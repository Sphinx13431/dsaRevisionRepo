from collections import deque


class Solution:
    def bfsOfGraph(self, V: int, adj: list[list[int]]) -> list[int]:
        """Return a breadth-first traversal, including every component."""
        visited = [False] * V
        traversal = []

        for start in range(V):
            if visited[start]:
                continue

            queue = deque([start])
            visited[start] = True
            while queue:
                node = queue.popleft()
                traversal.append(node)

                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

        return traversal


# TC: O(V + E), where E is the number of adjacency-list entries.
# SC: O(V) for the visited array and queue (excluding the result).