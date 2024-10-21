class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        def backtrack(i, cur_set):
            if i == len(s):
                return 0

            res = 0
            for j in range(i, len(s)):
                substr = s[i:j+1]
                if substr not in cur_set:
                    cur_set.add(substr)
                    res = max(res, 1 + backtrack(j + 1, cur_set))
                    cur_set.remove(substr)

            return res

        return backtrack(0, set())
