class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        adj = defaultdict(list)
        for city1, city2, dist in edges:
            adj[city1].append((city2, dist))
            adj[city2].append((city1, dist))

        res, min_count = -1, n
        for src in range(n):
            count = self._dijkstra(src, adj, distanceThreshold)
            if count <= min_count:
                res, min_count = src, count
        return res


    def _dijkstra(self, src: int, adj: dict, distance_threshold) -> int:
        
        heap = [(0, src)]   # dist, node
        visited = set()

        while heap:
            dist, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            for nei, next_dist in adj[node]:
                if dist + next_dist <= distance_threshold:
                    heapq.heappush(heap, (dist + next_dist, nei))
        
        return len(visited) - 1
