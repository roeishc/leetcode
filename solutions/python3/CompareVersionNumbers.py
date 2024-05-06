class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_split: list = version1.split('.')
        v2_split: list = version2.split('.')
        v1_len: int = len(v1_split)
        v2_len: int = len(v2_split)

        # pad the shorter list (version number with fewer dots) with 0's
        if v2_len < v1_len:
            v2_split += [0 for _ in range(v1_len - v2_len)]
        elif v1_len < v2_len:
            v1_split += [0 for _ in range(v2_len - v1_len)]

        i: int = 0
        for v1, v2 in zip(v1_split, v2_split):
            v1 = int(v1)
            v2 = int(v2)
            if v1 < v2:
                return -1
            elif v2 < v1:
                return 1
        return 0
        