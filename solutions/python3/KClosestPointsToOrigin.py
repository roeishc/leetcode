class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:k]

        
        # heap solution:
        
        # heap = []
        # for x, y in points:
        #     heapq.heappush(heap, (x**2 + y**2, x, y))
        
        # return [heapq.heappop(heap)[1:3] for _ in range(k)]
