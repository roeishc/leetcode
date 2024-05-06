class Solution:
    def getIntegerBinRepresentation(self, word: str) -> int:
        rep: int = 0
        a = ord('a')
        for ch in word:
            rep |= (1 << (ord(ch) - a))
        return rep


    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_int: int = self.getIntegerBinRepresentation(allowed)
        ans: int = 0
        temp: int = 0
        for word in words:
            temp = self.getIntegerBinRepresentation(word)
            if temp == temp & allowed_int:
                ans += 1
        return ans
            