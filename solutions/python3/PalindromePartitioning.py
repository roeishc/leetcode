class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        backtrack(s, 0, [], res)
        return res

def is_palindrome(s: str) -> bool:
    s_len_half = int(len(s)/2)
    return s[:s_len_half] == s[-1:-s_len_half-1:-1]

def backtrack(s: str, start: int, partition: List[str], res: List[List[str]]):
    if start == len(s):
        res.append(partition)
        return
    for end in range(start + 1, len(s) + 1):
        if is_palindrome(s[start:end]):
            backtrack(
                s = s,
                start = end,
                partition = partition + [s[start:end]],
                res = res)