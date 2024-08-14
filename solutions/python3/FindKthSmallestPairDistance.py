class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        def count_pairs_with_dist_smaller_than(dist):
            # count total number of pairs with a difference less than or equal to param `dist`
            l = res = 0
            for r in range(len(nums)):
                while nums[r] - nums[l] > dist:
                    l += 1
                res += r - l
            return res
            
        # binary search on the possible result (the kth smallest distance)
        l, r = 0, max(nums)
        while l < r:
            m = l + ((r - l) // 2)
            pairs = count_pairs_with_dist_smaller_than(m)
            if pairs >= k:
                r = m
            else:
                l = m + 1
        
        return l
