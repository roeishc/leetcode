class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        abs_sum = negatives = 0
        min_abs = float('inf')
        for row in matrix:
            for num in row:
                if num <= 0:
                    negatives += 1
                min_abs = min(min_abs, abs(num))
                abs_sum += abs(num)
        
        return abs_sum if negatives % 2 == 0 else abs_sum - abs(min_abs) * 2
