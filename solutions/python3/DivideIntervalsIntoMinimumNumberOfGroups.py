class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        current_intersection = []
        res = 0

        sorted_intervals = sorted(intervals)
        for start, end in sorted_intervals:
            while current_intersection and current_intersection[0] < start:
                heapq.heappop(current_intersection)
            heapq.heappush(current_intersection, end)
            res = max(res, len(current_intersection))
        
        return res
