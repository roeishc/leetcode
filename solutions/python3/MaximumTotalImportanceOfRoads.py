class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        
        freqs = defaultdict(int)
        for road in roads:
            freqs[road[0]] += 1
            freqs[road[1]] += 1
        
        cities = sorted(freqs.items(), key = lambda x : x[1])
        
        importances = []
        for i in range(len(cities)):
            importances.append((cities[-(i+1)][0], n - i))
        
        d = dict(importances)
        res = 0
        for road in roads:
            res += d[road[0]]
            res += d[road[1]]

        return res