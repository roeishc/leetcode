class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k or self.min_heap[0] < val:
            heapq.heappush(self.min_heap, val)
            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)
        return self.min_heap[0]


    # initial solution: created a heap with all elements. unnecessary, and resulted in time limit exceeded

    # def __init__(self, k: int, nums: List[int]):
    #     self.k = k
    #     self.max_heap = [-n for n in nums]
    #     heapq.heapify(self.max_heap)

    # def add(self, val: int) -> int:
    #     heappush(self.max_heap, -val)
    #     popped = []
    #     for _ in range(self.k):
    #         if not self.max_heap:
    #             for el in popped:
    #                 heapq.heappush(self.max_heap, el)
    #             return None
    #         popped.append(heapq.heappop(self.max_heap))
    #     res = -popped[-1]
    #     while popped:
    #         heapq.heappush(self.max_heap, popped.pop())
    #     return res

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)