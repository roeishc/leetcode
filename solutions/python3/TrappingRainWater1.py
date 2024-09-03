class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        water_in_i = [0] * n

        max_height_to_my_left = [0] * n
        max_height_to_my_left[0] = height[0]
        for i in range(1, n):
            max_height_to_my_left[i] = max(max_height_to_my_left[i - 1], height[i - 1])

        max_height_to_my_right = [0] * n
        max_height_to_my_right[-1] = height[-1]
        for i in range(n - 2, -1, -1):   # range(start, stop, step)
            max_height_to_my_right[i] = max(height[i + 1], max_height_to_my_right[i + 1])

        for i, bar in enumerate(height):
            if i == 0 or i == n - 1:
                continue
            water = min(
                max_height_to_my_left[i],
                max_height_to_my_right[i]
                ) - bar
            if water <= 0:
                continue
            water_in_i[i] = water

        return sum(water_in_i)
