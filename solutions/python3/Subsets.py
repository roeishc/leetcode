class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets: List[List[int]] = []
        self.generate_subsets(nums, 0, [], subsets)
        return subsets
    
    def generate_subsets(self, nums: List[int], index: int, subset: List[int], subsets: List[List[int]]) -> List[int]:

        if (index == len(nums)):
            subsets.append(deepcopy(subset))
            return
        
        subset.append(nums[index])
        self.generate_subsets(nums, index + 1, subset, subsets)

        subset.pop()
        self.generate_subsets(nums, index + 1, subset, subsets)