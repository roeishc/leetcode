class Solution:
    def check(self, nums: List[int]) -> bool:
        
        pivot = -1
        n = len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                pivot = i + 1
        
        if pivot == -1: # sorted without rotation
            return True

        # verify all elements to left of pivot are sorted in increasing order and greater than pivot
        if not self.is_non_decreasing_and_greather_than_num(nums[:pivot], nums[pivot]):
            return False

        # verify all elements to right of pivot are sorted in increasing order and greater than pivot
        if not self.is_non_decreasing_and_greather_than_num(nums[pivot:], nums[pivot]):
            return False

        # verify nums[-1] <= nums[0] for continuity in increasing order
        if nums[0] < nums[-1]:
            return False
        
        return True


    def is_non_decreasing_and_greather_than_num(self, nums: list[int], num: int) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1] or nums[i] < num:
                return False
        return True
