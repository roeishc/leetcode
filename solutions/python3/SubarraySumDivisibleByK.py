class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_mod = 0
        seen_mod = defaultdict(int)
        seen_mod[0] = 1
        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i]) % k
            res += seen_mod[prefix_mod]
            seen_mod[prefix_mod] += 1
        return res
