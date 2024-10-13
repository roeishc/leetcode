class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        k = len(nums)
        left = right = nums[0][0]
        min_heap = []
        for i in range(k):
            l = nums[i]
            left = min(left, l[0])
            right = max(right, l[0])
            heapq.heappush(min_heap, (l[0], i, 0))  # value, index of list in nums, index of value in l

        res = [left, right]
        while True:
            val, list_idx, val_idx = heapq.heappop(min_heap)
            val_idx += 1

            if val_idx == len(nums[list_idx]):
                return res

            next_val = nums[list_idx][val_idx]
            heapq.heappush(
                min_heap,
                (next_val, list_idx, val_idx)
            )

            right = max(right, next_val)
            left = min_heap[0][0]

            if right - left < res[1] - res[0]:
                res = [left, right]
