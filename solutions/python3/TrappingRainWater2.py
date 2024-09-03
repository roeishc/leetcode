class Solution:
    def trap(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1
        left_max, right_max = height[0], height[-1]
        res = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                res += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                res += right_max - height[right]

        return res
