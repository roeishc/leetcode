class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)

        res = 0
        for i in range(k):
            res -= max_heap[0]
            heapq.heapreplace(max_heap, -ceil(-max_heap[0] / 3))
        
        return res
