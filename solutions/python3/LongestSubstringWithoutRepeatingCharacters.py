class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = res = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            res = max(res, right - left + 1)
        
        return res
        
        
        # initial solution: messy. missed the mark
        
        # n = len(s)
        # if n == 0:
        #     return 0

        # left = right = 0
        # res = 1

        # while right < n:
        #     if left == right:
        #         cur_len = 1
        #         seen = set([s[left]])
        #         right += 1
        #     else:
        #         if s[right] in seen:    # the new character is already in the current window/substring
        #             if s[right] == s[left]: # edge case - don't remove from set, just increment
        #                 left += 1
        #                 right += 1
        #             else:
        #                 while s[left] != s[right]:
        #                     seen.remove(s[left])
        #                     left += 1
        #                 left += 1
        #                 cur_len = right - left + 1
        #                 right += 1
        #         else:   # the new character is not in the current substring
        #             cur_len += 1
        #             seen.add(s[right])
        #             res = max(res, cur_len)
        #             right += 1

        # return res
