class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        diff = sorted(enumerate(difficulty), key=lambda x: x[1])
        worker.sort()

        n = len(difficulty)
        res = 0
        i = 0
        wp = []

        for w in worker:
            while i < n and diff[i][1] <= w:
                heapq.heappush(wp, -profit[diff[i][0]])
                i += 1
            if wp:
                res += -wp[0]
            
        return res
