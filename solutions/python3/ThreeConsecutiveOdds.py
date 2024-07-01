class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        consecutives = 0
        for num in arr:
            consecutives = consecutives + 1 if num & 1 == 1 else 0
            if consecutives == 3:
                return True
        return False

        
        # trivial: check groups of 3 and the parity of each element
        # n = len(arr)
        # if n < 3:
        #     return False
        # for i in range(n - 2):
        #     if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
        #         return True
        # return False
        