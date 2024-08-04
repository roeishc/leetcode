class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        # time complexity: O(n^2logn)
        # space complexity: optimized with minimum heap: O(n), instead of O(n^2) in brute force
        
        mod_val = 10**9 + 7
        min_heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(min_heap)

        res = 0
        for seen in range(right):
            val, index_in_sorted_subarrays_sums = heapq.heappop(min_heap)
            if seen >= left - 1:
                res = (res + val) % mod_val
            if index_in_sorted_subarrays_sums + 1 < n:
                heapq.heappush(
                    min_heap,
                    (val + nums[index_in_sorted_subarrays_sums + 1], index_in_sorted_subarrays_sums + 1)
                    )

        return res


        # initial solution: brute force. O(n^2logn) time, O(n^2) space

        # mod_val = 10**9 + 7
        # sums = []
        
        # for start in range(n):
        #     cur_sum = 0
        #     for end in range(start, n):
        #         cur_sum = (cur_sum + nums[end]) % mod_val
        #         sums.append(cur_sum)
        
        # sums.sort()        
        # res = 0
        # for num in sums[left-1:right]:
        #     res = (res + num) % mod_val
        
        # return res
