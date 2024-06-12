class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums_len = len(nums)
        idx0 = 0
        idx2 = nums_len - 1
        temp: int

        for i in range(nums_len):
            while idx0 < nums_len and nums[idx0] == 0:
                idx0 += 1
            while idx2 > 0 and nums[idx2] == 2:
                idx2 -= 1
            if i < idx2 and nums[i] == 2:  # swap to the end of 0's
                temp = nums[i]
                nums[i] = nums[idx2]
                nums[idx2] = temp
            if idx0 < i and nums[i] == 0:  # swap to the beginning of 2's
                temp = nums[i]
                nums[i] = nums[idx0]
                nums[idx0] = temp
