class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()
        n = len(position)
        res = 0
        
        low = 1
        high = int(position[-1] / (m - 1)) + 1

        while low <= high:
            mid = low + (high - low) // 2
            if self.can_place_balls(mid, position, m):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return res


    def can_place_balls(self, x: int, position: List[int], m: int) -> bool:
        prev_ball_pos = position[0]
        balls_placed = 1
        for i in range(1, len(position)):
            curr_pos = position[i]
            if x <= curr_pos - prev_ball_pos:
                balls_placed += 1
                prev_ball_pos = curr_pos
            if balls_placed == m:
                return True
        return False
