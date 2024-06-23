class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        max_heap = []
        min_heap = []

        left = 0
        res = 0

        for right in range(len(nums)):
            heapq.heappush(max_heap, (-nums[right], right))
            heapq.heappush(min_heap, (nums[right], right))

            while -max_heap[0][0] - min_heap[0][0] > limit:
                left = min(max_heap[0][1], min_heap[0][1]) + 1
                while max_heap[0][1] < left:
                    heapq.heappop(max_heap)
                while min_heap[0][1] < left:
                    heapq.heappop(min_heap)
            
            res = max(res, right - left + 1)

        return res


        # first iteration of my soultion - passed the few sample tests.
        # happy to have figured out the gist of the solution using 2 heaps
        # and left & right pointers for a sliding window

        # left = 0
        # right = 0
        # n = len(nums)

        # max_heap = []
        # min_heap = []
        # i = 0
        # res = 0

        # while left <= right and i <= n:
        #     if i < n:
        #         heapq.heappush(max_heap, (-nums[i], i))     # save (value, index)
        #         heapq.heappush(min_heap, (nums[i], i))      # save (value, index)
        #     max_val = (-max_heap[0][0], max_heap[0][1])
        #     min_val = min_heap[0]

        #     if abs(max_val[0] - min_val[0]) <= limit:
        #         right += 1
        #     else:
        #         if max_val[1] == left:
        #             heapq.heappop(max_heap)
        #             left += 1
        #         elif min_val[1] == left:
        #             heapq.heappop(min_heap)
        #             left += 1

        #     res = max(res, right - left + 1)
        #     i += 1

        # return res