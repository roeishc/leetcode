class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        direction_map = {
            "n": (0, 1),
            "s": (0, -1),
            "e": (1, 0),
            "w": (-1, 0)
        }
        cur_direction = "n"
        cur_location = (0, 0)

        obs_set = set([(x, y) for x, y in obstacles])
        furthest = 0

        for command in commands:
            if command > 0:
                while (
                    command > 0 and
                    (cur_location[0] + direction_map[cur_direction][0], cur_location[1] + direction_map[cur_direction][1]) not in obs_set
                ):
                    command -= 1
                    cur_location = (cur_location[0] + direction_map[cur_direction][0], cur_location[1] + direction_map[cur_direction][1])
                    furthest = max(furthest, cur_location[0] * cur_location[0] + cur_location[1] * cur_location[1])

            else:   # is a turn
                cur_direction = self._change_direction(cur_direction, command)

        return furthest


    def _change_direction(self, cur: str, turn: int) -> str:
        directions = ["n", "e", "s", "w"]
        i = directions.index(cur)
        if turn == -1:
            return directions[(i + 1) % 4]
        elif turn == -2:
            return directions[(i - 1) % 4]
        else:
            return None
