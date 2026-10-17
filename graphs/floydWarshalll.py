class Solution:
    def floydWarshall(self, dist: list[list[float]]) -> list[list[float]]:
        """Compute all-pairs shortest paths in place and return dist.

        Use float("inf") for missing edges and 0 on the diagonal. Negative
        cycles can be detected after the run by checking for a negative
        diagonal entry.
        """
        vertices = len(dist)
        infinity = float("inf")

        for intermediate in range(vertices):
            for source in range(vertices):
                if dist[source][intermediate] == infinity:
                    continue
                for destination in range(vertices):
                    if dist[intermediate][destination] == infinity:
                        continue
                    candidate = (
                        dist[source][intermediate] + dist[intermediate][destination]
                    )
                    if candidate < dist[source][destination]:
                        dist[source][destination] = candidate

        return dist


# TC: O(V^3).
# SC: O(1) auxiliary; the input distance matrix is updated in place.