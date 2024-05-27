class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        nums_len = len(nums)
        for i in range(nums_len):
            # first: check if there are x numbers greater than or equal to x
            # second: verify that the previous element (if exists [i==0 first]) is smaller than current
            # value being checked
            if nums_len - i <= nums[i] and (i == 0 or nums[i-1] < nums_len - i):
                return nums_len - i
        return -1
        