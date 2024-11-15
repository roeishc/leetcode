class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        N = len(arr)
        r = N - 1
        while r > 0 and arr[r - 1] <= arr[r]:
            r -= 1

        res = r

        l = 0
        while l < r:
            while r < N and arr[l] > arr[r]:
                r += 1
            res = min(res, r - l - 1)
            if arr[l] > arr[l + 1]:
                break
            l += 1
        
        return res
