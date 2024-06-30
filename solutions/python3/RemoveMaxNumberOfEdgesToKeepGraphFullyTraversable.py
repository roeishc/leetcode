class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        if len(edges) == 1 and edges[0][0] != 3:    # edge case with only 1 edge which isn't type 3 (both)
            return -1

        alice, bob = UnionFind(n), UnionFind(n)
        count = 0   # how many edges we need to keep, to keep the graph fully connected for both Alice & Bob

        for t, src, dst in edges:
            if t == 3:
                count += max(alice.union(src, dst), bob.union(src, dst))
            
        for t, src, dst in edges:
            if t == 1:
                count += alice.union(src, dst)
            elif t == 2:
                count += bob.union(src, dst)
        
        if bob.is_connected() and alice.is_connected:
            return len(edges) - count
        
        return -1


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)

    def find(self, x: int) -> int:
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1: int, x2: int) -> int:
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return 0
        if self.rank[p1] > self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.par[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.par[p1] = p2
        self.n -= 1
        return 1
    
    def is_connected(self) -> bool:
        return self.n == 1