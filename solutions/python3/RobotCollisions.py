class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
        if "L" in directions and "R" not in directions or "R" in directions and "L" not in directions:
            return healths

        pdh = sorted([list(e) for e in zip(positions, directions, healths, range(len(healths)))], key=lambda x: x[0])
        i = 0

        print(pdh)

        while i < len(pdh) - 1:
            if pdh[i][1] == "R" and pdh[i + 1][1] == "L":  # collision
                if pdh[i][2] > pdh[i + 1][2]:   # "R" won (current index)
                    pdh[i][2] -= 1
                    pdh.pop(i + 1)
                elif pdh[i][2] < pdh[i + 1][2]: # "L" win (next index)
                    pdh[i + 1][2] -= 1
                    pdh.pop(i)
                    i = max(0, i - 1)
                else:  # pop both
                    pdh.pop(i + 1)
                    pdh.pop(i)
                    i = max(0, i - 1)
            else:
                i += 1

        if not pdh:
            return []

        pdh = sorted(pdh, key=lambda x: x[3])  # sort according to original healths indices
        return list(list(zip(*pdh))[2])
