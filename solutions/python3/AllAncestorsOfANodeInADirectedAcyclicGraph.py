class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        can_reach = [[] for _ in range(n)]  # can_reach[3] - list of all nodes that can reach 3
        for edge in edges:
            can_reach[edge[1]].append(edge[0])

        res = []
        for i in range(n):
            ancestors = []
            visited = set()
            self.find_children(i, can_reach, visited)   # find children of i in the reversed graph
            for node in range(n):
                if node == i:
                    continue
                if node in visited:
                    ancestors.append(node)
            res.append(ancestors)

        return res

    def find_children(self, root: int, can_reach: List[List[int]], visited: set):
        visited.add(root)
        for node in can_reach[root]:
            if node not in visited:
                self.find_children(node, can_reach, visited)


        
        # First iteration of my solution - solved only some of the tests
        
        # res = [[] for i in range(n)]

        # for edge in edges:
        #     res[edge[1]].append(edge[0])

        # for i in range(len(res)):
        #     for source in res[i]:
        #         res[i] += res[source]
        #         res[i] = list(set(res[i]))  # eliminate duplicates
        #         res[i].sort()

        # return res