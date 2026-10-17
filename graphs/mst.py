import heapq


class Solution:
    def primMST(
        self, V: int, adj: list[list[tuple[int, int]]], start: int = 0
    ) -> tuple[int, list[tuple[int, int, int]]]:
        """Return (weight, edges) for a minimum spanning tree using Prim's.

        The undirected graph must be represented in both directions in adj.
        Raises ValueError if the graph is disconnected.
        """
        if V == 0:
            return 0, []
        if not 0 <= start < V:
            raise ValueError("start must be a valid vertex")

        visited = [False] * V
        min_heap = [(0, start, -1)]
        total_weight = 0
        mst_edges = []

        while min_heap and len(mst_edges) < V - 1:
            weight, node, parent = heapq.heappop(min_heap)
            if visited[node]:
                continue

            visited[node] = True
            total_weight += weight
            if parent != -1:
                mst_edges.append((parent, node, weight))

            for neighbor, edge_weight in adj[node]:
                if not visited[neighbor]:
                    heapq.heappush(min_heap, (edge_weight, neighbor, node))

        if len(mst_edges) != V - 1:
            raise ValueError("a minimum spanning tree does not exist for a disconnected graph")
        return total_weight, mst_edges

    def kruskalMST(
        self, V: int, edges: list[tuple[int, int, int]]
    ) -> tuple[int, list[tuple[int, int, int]]]:
        """Return (weight, edges) for a minimum spanning tree using Kruskal's.

        Each edge is (u, v, weight). Raises ValueError if disconnected.
        """
        if V == 0:
            return 0, []

        parent = list(range(V))
        size = [1] * V

        def find(node: int) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        total_weight = 0
        mst_edges = []
        for u, v, weight in sorted(edges, key=lambda edge: edge[2]):
            root_u = find(u)
            root_v = find(v)
            if root_u == root_v:
                continue

            if size[root_u] < size[root_v]:
                root_u, root_v = root_v, root_u
            parent[root_v] = root_u
            size[root_u] += size[root_v]
            total_weight += weight
            mst_edges.append((u, v, weight))

            if len(mst_edges) == V - 1:
                break

        if len(mst_edges) != V - 1:
            raise ValueError("a minimum spanning tree does not exist for a disconnected graph")
        return total_weight, mst_edges


# Prim's: TC O(E log V) for a simple graph, SC O(V + E) including its heap.
# Kruskal's: TC O(E log E), SC O(V + E) including the sorted edge list.