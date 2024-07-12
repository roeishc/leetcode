class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        if x < y:
            s = s[::-1]
            x, y = y, x
        
        a_count, b_count, score = 0, 0, 0

        for i in range(len(s)):
            if s[i] == "a":
                a_count += 1
            elif s[i] == "b":
                if a_count > 0:     # can form at least one pair of "ab"
                    a_count -= 1    # "remove" one "a"
                    score += x
                else:
                    b_count += 1
            else:   # handle case of "ba" pairs (if any can be formed)
                score += min(a_count, b_count) * y
                a_count = b_count = 0

        score += min(a_count, b_count) * y
        
        return score


        # first iteration of my solution: time limit exceeded with 10^5 characters
        
        # score = 0

        # if x > y:   # greedily remove all "ab" before "ba"
        #     while "ab" in s or "ba" in s:
        #         idx = s.find("ab")
        #         while idx != -1:
        #             score += x
        #             s = s[0:idx] + s[idx + 2:]
        #             idx = s.find("ab")
        #         idx = s.find("ba")
        #         while idx != -1:
        #             score += y
        #             s = s[0:idx] + s[idx + 2:]
        #             idx = s.find("ba")
        # else:       # greedily remove all "ba" before "ab"
        #     while "ab" in s or "ba" in s:
        #         idx = s.find("ba")
        #         while idx != -1:
        #             score += y
        #             s = s[0:idx] + s[idx + 2:]
        #             idx = s.find("ba")
        #         idx = s.find("ab")
        #         while idx != -1:
        #             score += x
        #             s = s[0:idx] + s[idx + 2:]
        #             idx = s.find("ab")

        # return score
