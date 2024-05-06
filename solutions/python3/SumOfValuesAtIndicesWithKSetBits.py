class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        # binary_nums = [str(bin(i))[2:] for i in nums]
        sum = 0
        for i, num in enumerate(nums):
            if i.bit_count() == k:
                sum += num
        return sum