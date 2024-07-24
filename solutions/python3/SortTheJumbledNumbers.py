class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        mapped = []
        for i, num in enumerate(nums):
            temp = ""
            num_str = str(num)
            for c in num_str:
                temp += str(mapping[int(c)])
            mapped.append((int(temp), i))
        mapped = sorted(mapped)
        indexes = list(list(zip(*mapped))[1])

        return [nums[i] for i in indexes]
