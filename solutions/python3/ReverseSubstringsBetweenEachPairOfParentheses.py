class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        n = len(s)
        open_indices = []
        pair = [0] * n

        for i, c in enumerate(s):
            if c == "(":
                open_indices.append(i)
            elif c == ")":
                j = open_indices.pop()
                pair[i] = j
                pair[j] = i

        current = 0
        res = ""
        direction = 1

        while current < n:
            if s[current] == "(" or s[current] == ")":
                current = pair[current]
                direction *= -1
            else:
                res += s[current]
            current += direction
        
        return res


        # first solution: stack of stacks, O(n^2)

        # stacks: List[List[str]] = []
        # res = ""

        # for i in range(len(s)):
        #     if s[i] != "(" and s[i] != ")" and not stacks:
        #         res += s[i]
        #     elif s[i] == "(":
        #         stacks.append([])
        #     elif s[i] != ")":   # "regular" chars
        #         stacks[-1].append(s[i])
        #     else:   # is ")"
        #         if len(stacks) == 1:
        #             while stacks[-1]:
        #                 res += stacks[-1].pop()
        #         else:   # greater than 1
        #             while stacks[-1]:
        #                 stacks[-2].append(stacks[-1].pop())
        #         stacks.pop()

        # return res
