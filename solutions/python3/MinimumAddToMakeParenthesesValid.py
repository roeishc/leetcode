class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        opening = closing_without_opening = 0

        for c in s:
            if c == "(":
                opening += 1
            else:
                if opening == 0:
                    closing_without_opening += 1
                opening = max(opening - 1, 0)

        return opening + closing_without_opening
        