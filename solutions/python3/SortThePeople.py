class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pairs = sorted(list(zip(heights, names)), reverse=True)
        return list(list(zip(*pairs))[1])
