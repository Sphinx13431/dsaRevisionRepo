class Solution:
    def dfs(
        self,
        node: int,
        adj: list[list[int]],
        state: list[int],
        ordering: list[int],
    ) -> bool:
        state[node] = 1
        for neighbor in adj[node]:
            if state[neighbor] == 1:
                return False
            if state[neighbor] == 0 and not self.dfs(
                neighbor, adj, state, ordering
            ):
                return False
        state[node] = 2
        ordering.append(node)
        return True

    def topoSort(self, V: int, adj: list[list[int]]) -> list[int]:
        """Return a DFS-based topological ordering, or [] if cyclic."""
        # 0 = unseen, 1 = active in the current DFS path, 2 = finished.
        state = [0] * V
        ordering = []

        for start in range(V):
            if state[start] == 0 and not self.dfs(start, adj, state, ordering):
                return []
        ordering.reverse()
        return ordering


# TC: O(V + E).
# SC: O(V) for traversal state, recursion stack, and result.