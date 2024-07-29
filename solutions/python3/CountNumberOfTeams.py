class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        n = len(rating)
        if n < 3:
            return 0

        res = 0
        for mid in range(1, n - 1):
            smaller_before = greater_before = smaller_after = greater_after = 0
            for left in range(0, mid):
                if rating[left] < rating[mid]:
                    smaller_before += 1
                else:
                    greater_before += 1
            for right in range(mid + 1, n):
                if rating[mid] < rating[right]:
                    greater_after += 1
                else:
                    smaller_after += 1

            res += smaller_before * greater_after + smaller_after * greater_before

        return res
