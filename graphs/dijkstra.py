import heapq


class Solution:
    def dijkstra(
        self, V: int, adj: list[list[tuple[int, int]]], src: int
    ) -> list[float]:
        """Return shortest distances from src in a non-negative weighted graph.

        Each adjacency entry is (neighbor, weight). Raises ValueError if any
        edge has a negative weight.
        """
        if not 0 <= src < V:
            raise ValueError("src must be a valid vertex")
        if any(weight < 0 for neighbors in adj for _, weight in neighbors):
            raise ValueError("Dijkstra's algorithm requires non-negative weights")

        infinity = float("inf")
        distance = [infinity] * V
        distance[src] = 0
        min_heap = [(0, src)]

        while min_heap:
            current_distance, node = heapq.heappop(min_heap)
            if current_distance != distance[node]:
                continue

            for neighbor, weight in adj[node]:
                candidate = current_distance + weight
                if candidate < distance[neighbor]:
                    distance[neighbor] = candidate
                    heapq.heappush(min_heap, (candidate, neighbor))

        return distance


# TC: O((V + E) log V) with a binary heap.
# SC: O(V) auxiliary space for distances and the heap.