class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        adj = defaultdict(list)
        for src, dest, costt in zip(original, changed, cost):
            adj[src].append((dest, costt))

        res = 0
        shortest_path = {}  # to save results of shortest paths to avoid recalculations. key: (src, dest). value: shortest path
        for s, t in zip(source, target):
            if (s, t) in shortest_path:
                res += shortest_path[(s, t)]
                continue
            s_to_c_cost = self._get_lightest_path(s, t, adj)
            if s_to_c_cost == -1:
                return -1
            shortest_path[(s, t)] = s_to_c_cost
            res += s_to_c_cost

        return res

    def _get_lightest_path(self, src: str, dest: str, adj: dict) -> int:

        heap = [(0, src)]
        visited = set()

        while heap:
            cost, current_node = heapq.heappop(heap)
            if current_node == dest:
                return cost
            if current_node in visited:
                continue
            visited.add(current_node)
            for nei, nei_cost in adj[current_node]:
                heapq.heappush(heap, (cost + nei_cost, nei))

        return -1
