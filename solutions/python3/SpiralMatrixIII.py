class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        matrix_coordinates = set()
        for i in range(rows):
            for j in range(cols):
                matrix_coordinates.add((i, j))

        steps_to_take = 1
        directions = {
            "right": (0, 1),
            "down": (1, 0),
            "left": (0, -1),
            "up": (-1, 0)
        }

        res = []
        current = (rStart, cStart)

        while matrix_coordinates:
            for i, (direction, step) in enumerate(directions.items()):
                for _ in range(steps_to_take):
                    if current in matrix_coordinates:
                        res.append(list(current))
                        matrix_coordinates.remove(current)
                    current = (current[0] + step[0], current[1] + step[1])
                if i % 2 == 1:
                    steps_to_take += 1
            
        return res
