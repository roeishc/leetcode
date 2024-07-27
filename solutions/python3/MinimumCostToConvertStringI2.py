class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        n = 26  # lower case English letters
        self.letters_to_ints = {chr(97+i): i for i in range(n)}  # map letter to int value in inclusive range [0, 25]

        adj = {}
        for src, dest, costt in zip(original, changed, cost):
            if (src, dest) in adj:  # in case there are multiple edges from src to dest
                adj[(src, dest)] = min(adj[(src, dest)], costt)
            else:
                adj[(src, dest)] = costt

        dist = self._floyd_warshall(adj, original, changed, n)

        res = 0
        for s, t in zip(source, target):
            costt = dist[self.letters_to_ints[s]][self.letters_to_ints[t]]
            if costt == float('inf'):
                return -1
            res += costt

        return res


    def _floyd_warshall(self, adj: dict, original: List[str], changed: List[str], n: int) -> List[List]:

        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for s, t in zip(original, changed):
            dist[self.letters_to_ints[s]][self.letters_to_ints[t]] = adj[(s, t)]

        for k in range(n):
            for j in range(n):
                for i in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        return dist
