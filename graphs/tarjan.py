
from typing import List


class Solution:
    def __init__(self):
        self.time = 0

    def dfs(
        self,
        graph: List[List[int]],
        visited: List[bool],
        tin: List[int],
        lowTin: List[int],
        bridges: List[List[int]],
        node: int,
        parent: int
    ):
        visited[node] = True

        # tin[node] = discovery time of this node during DFS.
        # lowTin[node] = earliest discovery time reachable from this node's
        # subtree using tree edges and at most one back edge.
        self.time += 1
        tin[node] = lowTin[node] = self.time

        for i in graph[node]:

            # Ignore the edge back to the parent.
            # In an undirected graph, every tree edge appears in both directions.
            if i == parent:
                continue

            if not visited[i]:

                # Explore the child's subtree first.
                self.dfs(
                    graph, visited, tin, lowTin,
                    bridges, i, node
                )

                # The child's subtree may be able to reach an ancestor
                # of the current node. Propagate that earliest discovery time.
                lowTin[node] = min(lowTin[node], lowTin[i])

                # If the child's subtree cannot reach the current node
                # or any ancestor of it through a back edge, this edge
                # is a bridge.
                #
                # lowTin[i] > tin[node] means removing (node, i)
                # disconnects the child's subtree from the rest of the graph.
                if lowTin[i] > tin[node]:
                    bridges.append([node, i])

            else:
                # A visited neighbor other than the parent is a back edge.
                # Use tin[i], not lowTin[i], because this edge reaches
                # the neighbor itself, not necessarily its entire subtree.
                lowTin[node] = min(lowTin[node], tin[i])

    def tarjans(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # Build the adjacency list for the undirected graph.
        graph = [[] for _ in range(n)]

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        timeOfInsertion = [0] * n
        lowestTime = [0] * n
        bridges = []

        # Reset the timer for every invocation.
        self.time = 0

        # Start DFS from every unvisited node to handle disconnected graphs.
        for node in range(n):
            if not visited[node]:
                self.dfs(
                    graph,
                    visited,
                    timeOfInsertion,
                    lowestTime,
                    bridges,
                    node,
                    -1
                )

        return bridges


# Time Complexity: O(V + E)
# Every vertex is visited once, and every undirected edge is examined
# a constant number of times during DFS.

# Space Complexity: O(V + E)
# Adjacency list: O(V + E)
# Visited, tin, lowTin arrays: O(V)
# DFS recursion stack: O(V) in the worst case.
# Bridge storage: O(E) in the worst case.


'''
The key idea to remember
- tin[node] — when was this node first visited?
- lowTin[node] — how early can this node's subtree reach in the DFS discovery order?
- Bridge condition: lowTin[child] > tin[parent]
'''