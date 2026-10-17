class Solution:
    def dfsOfGraph(self, V: int, adj: list[list[int]]) -> list[int]:
        """Return a depth-first traversal, including every component."""
        visited = [False] * V
        traversal = []

        for start in range(V):
            if visited[start]:
                continue

            stack = [start]
            visited[start] = True
            while stack:
                node = stack.pop()
                traversal.append(node)

                # Reverse the neighbors so traversal follows adjacency order.
                for neighbor in reversed(adj[node]):
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)

        return traversal


# TC: O(V + E), where E is the number of adjacency-list entries.
# SC: O(V) for the visited array and traversal stack (excluding the result).