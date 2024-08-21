class Solution:
    def strangePrinter(self, s: str) -> int:
        
        s = "".join(c for c, _ in itertools.groupby(s)) # remove consecutive duplicates

        cache = {}

        def minimum_turns(start, end):
            if start > end:
                return 0
            if (start, end) in cache:
                return cache[(start, end)]
            
            min_turns = 1 + minimum_turns(start + 1, end)

            for k in range(start + 1, end + 1):
                if s[k] == s[start]:
                    turns_with_match = minimum_turns(start, k - 1) + minimum_turns(k + 1, end)
                    min_turns = min(min_turns, turns_with_match)

            cache[(start, end)] = min_turns
            return min_turns

        return minimum_turns(0, len(s) - 1)
