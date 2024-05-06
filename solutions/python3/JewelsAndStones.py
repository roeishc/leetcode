class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count: int = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        return count
        