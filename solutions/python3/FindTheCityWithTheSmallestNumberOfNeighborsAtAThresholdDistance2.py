class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        adj = {}
        for city1, city2, dist in edges:
            if (city1, city2) in adj:
                adj[(city1, city2)] = min(adj[(city1, city2)], dist)
                adj[(city2, city1)] = min(adj[(city2, city1)], dist)
            else:
                adj[(city1, city2)] = dist
                adj[(city2, city1)] = dist

        dist = self._floyd_warshall(adj, n)

        min_cities_reached, city_res = n, -1
        for src in range(n):
            from_cur = 0
            for dest in range(n):
                if src == dest:
                    continue
                if dist[src][dest] <= distanceThreshold:
                    from_cur += 1
            if from_cur <= min_cities_reached:
                min_cities_reached = from_cur
                city_res = src

        return city_res

    def _floyd_warshall(self, adj: dict, n: int) -> List[List]:

        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for (src, dest), d in adj.items():
            dist[src][dest] = d

        for k in range(n):
            for j in range(n):
                for i in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        return dist
