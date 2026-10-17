class Solution:
    def bellmanFord(
        self, V: int, edges: list[tuple[int, int, int]], src: int
    ) -> tuple[list[float], bool]:
        """Return (distances, has_reachable_negative_cycle).

        Each edge is (u, v, weight). Vertices unreachable from src retain
        float("inf"); a reachable negative cycle is reported by the boolean.
        """
        if not 0 <= src < V:
            raise ValueError("src must be a valid vertex")

        infinity = float("inf")
        distance = [infinity] * V
        distance[src] = 0

        for _ in range(V - 1):
            updated = False
            for u, v, weight in edges:
                if distance[u] != infinity and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                    updated = True
            if not updated:
                break

        for u, v, weight in edges:
            if distance[u] != infinity and distance[u] + weight < distance[v]:
                return distance, True
        return distance, False


# TC: O(V * E).
# SC: O(V) auxiliary space for distances.