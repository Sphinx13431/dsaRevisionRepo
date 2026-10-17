from collections import deque


class Solution:
    def topoSort(self, V: int, adj: list[list[int]]) -> list[int]:
        """Return a topological ordering, or [] if the graph has a cycle."""
        indegree = [0] * V
        for node in range(V):
            for neighbor in adj[node]:
                indegree[neighbor] += 1

        queue = deque(node for node in range(V) if indegree[node] == 0)
        ordering = []

        while queue:
            node = queue.popleft()
            ordering.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return ordering if len(ordering) == V else []


# TC: O(V + E).
# SC: O(V) for indegrees, queue, and result.