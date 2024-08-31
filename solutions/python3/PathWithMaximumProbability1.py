class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj = defaultdict(set)
        for i, (src, dst) in enumerate(edges):
            adj[src].add((dst, succProb[i]))
            adj[dst].add((src, succProb[i]))

        max_heap = [(-1, start_node)]
        visited = set()

        while max_heap:
            total_prob, cur = heapq.heappop(max_heap)
            visited.add(cur)

            if cur == end_node:
                return -total_prob
            
            for nei, nei_prob in adj[cur]:
                if nei not in visited:
                    heapq.heappush(max_heap, (total_prob * nei_prob, nei))

        return 0
