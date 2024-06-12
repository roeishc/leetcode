class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # count frequencies of 0, 1, 2
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1
        # place the elements in nums according to theri frequencies
        idx = 0
        for val in range(3):
            while freqs[val] > 0:
                nums[idx] = val
                idx += 1
                freqs[val] -= 1
        