class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        if not edges:
            if n == 1:
                return 0
            return -1

        is_dest = [True] * n
        for src, dest in edges:
            is_dest[dest] = False
        
        if is_dest.count(True) == 1:
            return is_dest.index(True)
    
        return -1
