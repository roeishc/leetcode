class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums_string = [str(num) for num in nums]

        nums_string.sort(key = lambda a: a * 10, reverse=True)  # the constraint is nums[i] <= 10^9, so we need up to 10 digits to compare

        if nums_string[0] == "0":   # if the "MSB" is 0, return 0
            return "0"

        return "".join(nums_string)
