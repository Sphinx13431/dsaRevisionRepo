class DSU:
    """Disjoint Set Union with path compression and union by size."""

    def __init__(self, n: int) -> None:
        if n < 0:
            raise ValueError("n must be non-negative")
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, node: int) -> int:
        """Return the representative of node's set."""
        if not 0 <= node < len(self.parent):
            raise IndexError("node is outside the disjoint set")
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, first: int, second: int) -> bool:
        """Merge two sets; return True only if they were previously separate."""
        root_first = self.find(first)
        root_second = self.find(second)
        if root_first == root_second:
            return False

        if self.size[root_first] < self.size[root_second]:
            root_first, root_second = root_second, root_first
        self.parent[root_second] = root_first
        self.size[root_first] += self.size[root_second]
        return True


# TC: O(alpha(N)) amortized per find/union operation, where alpha is the
# inverse Ackermann function.
# SC: O(N) for parent and size arrays.