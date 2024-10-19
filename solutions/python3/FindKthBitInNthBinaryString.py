class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        if n == 1:
            return "0"

        middle_index = (2 ** n) // 2

        if k == middle_index:
            return "1"
        elif k < middle_index:
            return self.findKthBit(n - 1, k)
        else:
            bit = self.findKthBit(n - 1, (middle_index - k) % middle_index) # kth bit from the end (to save time instead of reversing)
            return "1" if bit == "0" else "0"
