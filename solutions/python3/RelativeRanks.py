class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        cpy: list = deepcopy(score)
        cpy.sort(reverse=True)
        ranks: dict = {}
        res: list = [None] * len(score)
        
        for i, val in enumerate(cpy):
            if i == 0:
                ranks[val] = "Gold Medal"
            elif i == 1:
                ranks[val] = "Silver Medal"
            elif i == 2:
                ranks[val] = "Bronze Medal"
            else:
                ranks[val] = str(i + 1)

        for i, val in enumerate(score):
            res[i] = ranks[val]
        
        return res
        