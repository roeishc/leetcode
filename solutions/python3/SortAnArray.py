class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        return self._merge_sort(nums)


    def _merge_sort(self, nums: List[int]) -> List[int]:

        n = len(nums)

        if n == 1:
            return nums
        
        mid = len(nums) // 2
        
        left = self._merge_sort(nums[:mid])
        right = self._merge_sort(nums[mid:])

        return self._merge(left, right)

        
    def _merge(self, arr1: List[int], arr2: List[int]) -> List[int]:

        idx1 = idx2 = idx_res = 0
        len1, len2 = len(arr1), len(arr2)
        res = [0] * (len1 + len2)

        while idx1 < len1 and idx2 < len2:
            if arr1[idx1] < arr2[idx2]:
                res[idx_res] = arr1[idx1]
                idx1 += 1
            else:
                res[idx_res] = arr2[idx2]
                idx2 += 1
            idx_res += 1
        
        while idx1 < len1:
            res[idx_res] = arr1[idx1]
            idx1 += 1
            idx_res += 1

        while idx2 < len2:
            res[idx_res] = arr2[idx2]
            idx2 += 1
            idx_res += 1
        
        return res
