class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_bin = str(bin(start))[2:]
        goal_bin = str(bin(goal))[2:]
        
        start_len = len(start_bin)
        goal_len = len(goal_bin)
        max_len = start_len

        if start_len < goal_len:
            start_bin = '0' * (goal_len - start_len) + start_bin
            max_len = goal_len
        elif goal_len < start_len:
            goal_bin = '0' * (start_len - goal_len) + goal_bin

        ans = 0
        for i in range(max_len):
            if start_bin[i] != goal_bin[i]:
                ans += 1
        
        return ans
        