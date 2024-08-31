class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        max_probability = [0] * n
        max_probability[start_node] = 1

        for i in range(n - 1):
            updated = False
            for j, (src, dst) in enumerate(edges):
                path_probability = succProb[j]
                if max_probability[src] < max_probability[dst] * path_probability:
                    max_probability[src] = max_probability[dst] * path_probability
                    updated = True
                if max_probability[dst] < max_probability[src] * path_probability:
                    max_probability[dst] = max_probability[src] * path_probability
                    updated = True
            if not updated:
                break
        
        return max_probability[end_node]
