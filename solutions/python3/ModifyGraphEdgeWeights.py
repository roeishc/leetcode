class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:

        def dijkstra():
            self._update_adj(edges)
            min_heap = [(0, source)]
            visited = set()
            while min_heap:
                total_distance, node = heapq.heappop(min_heap)
                visited.add(node)
                if node == destination:
                    return total_distance
                for nei, w in self.adj[node]:
                    if nei not in visited and w != -1:
                        heapq.heappush(min_heap, (total_distance + w, nei))
            return INF
        
        INF = 1000000005
        shortest_path = dijkstra()

        if shortest_path < target:  # if unreachable, can't modify any -1's to make reachable
            return []

        if shortest_path == target: # if already reachable, make sure that any -1's aren't a problem after modification
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = INF
            return edges
        
        if shortest_path > target:  # if reachable with -1's, check modifications of -1's for reachability
            if (destination, -1) in self.adj[source]:   # to save time, if there's an edge from src to dst with weight -1, use it
                for edge in edges:
                    if (
                        edge[0] == source and edge[1] == destination and edge[2] == -1
                        or
                        edge[1] == source and edge[0] == destination and edge[2] == -1
                        ):
                        edge[2] = target
                    elif edge[2] == -1:
                        edge[2] = INF
                return edges
            else:   # there isn't an edge from src to dst with weight -1
                modded = False
                for edge in edges:
                    if edge[2] > 0:
                        continue
                    edge[2] = INF if modded else 1
                    if not modded:  # make sure to change exactly one edge (will skip this statement if modded is true)
                        self._update_adj(edges)
                        new_shortest_path = dijkstra()
                        if new_shortest_path <= target:
                            modded = True
                            edge[2] += target - new_shortest_path
                return edges if modded else []


    def _update_adj(self, edges):
            self.adj = defaultdict(set)
            for s, d, w in edges:
                self.adj[s].add((d, w))
                self.adj[d].add((s, w))
