class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [0] * n
        nums[0] = start
        res = nums[0]
        for i in range(1, n):
            nums[i] = start + 2 * i
            res ^= nums[i]
        return res