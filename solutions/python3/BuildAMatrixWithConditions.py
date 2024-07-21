class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        row_order = self._topological_sort(rowConditions, k)
        col_order = self._topological_sort(colConditions, k)

        if not row_order or not col_order:
            return []

        val_to_row = {n:i for i, n in enumerate(row_order)}
        val_to_col = {n:i for i, n in enumerate(col_order)}

        res = [[0] * k for _ in range(k)]

        for num in range(1, k + 1):
            row, col = val_to_row[num], val_to_col[num]
            res[row][col] = num

        return res


    def _dfs(self, src: int, adj: dict, visited: set, current_path: set, order: List[int]) -> bool:
        """
        src: int
            The DFS's source node.
        adj: dictionary
            Adjacency "list" (where we can go from the current node).
            (it's a dictionary, but the usual name used is adjacency list)
        visited: set
            Set of all visited nodes in the algorithm so far. Starting empty, finishing will all nodes.
        current_path: set
            Set of all nodes in the current path.
        order: List[int]
            List of all the nodes we visited, in the order we visited them.
        """
        
        if src in current_path: # cycle detected
            return False
        if src in visited:
            return True
        
        visited.add(src)
        current_path.add(src)

        for nei in adj[src]:
            if not self._dfs(nei, adj, visited, current_path, order):   # if cycle detected
                return False
        
        current_path.remove(src)
        order.append(src)

        return True


    def _topological_sort(self, edges: List[int], k: int) -> List[int]:
        
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)

        visited, path = set(), set()
        order = []
        
        for src in range(1, k + 1):
            if not self._dfs(src, adj, visited, path, order):
                return []

        return order[::-1]
