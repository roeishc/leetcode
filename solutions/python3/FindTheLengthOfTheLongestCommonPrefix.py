class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        if len(arr1) > len(arr2):   # make sure arr1 is the shortest arr
            arr1, arr2 = arr2, arr1

        prefix_set = set()
        for num in arr1:
            while num and num not in prefix_set:
                prefix_set.add(num)
                num //= 10

        res = 0

        for num in arr2:
            while num and num not in prefix_set:
                num= num // 10
            if num:
                res = max(res, len(str(num)))
        
        return res
