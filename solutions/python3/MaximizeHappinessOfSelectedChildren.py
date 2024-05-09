class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True) # sorting: O(nlogn)
        res = 0
        for i in range(k): # take first k (largest) elements: O(k)
            res += max(happiness[i] - i, 0)
        return res
        