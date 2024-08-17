class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        ROWS, COLS = len(points), len(points[0])
        row = points[0]

        for r in range(1, ROWS):
            next_row = points[r].copy()
            from_left, from_right = [0] * COLS, [0] * COLS

            from_left[0] = row[0]
            for c in range(1, COLS):
                from_left[c] = max(row[c], from_left[c - 1] - 1)

            from_right[COLS - 1] = row[COLS - 1]
            for c in range(COLS - 2, -1, -1):
                from_right[c] = max(row[c], from_right[c + 1] - 1)

            for c in range(COLS):
                next_row[c] += max(from_left[c], from_right[c])
            row = next_row

        return max(row)
