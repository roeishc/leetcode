# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        self.pairs = 0

        self._dfs(root, distance)

        return self.pairs
    

    def _dfs(self, root: TreeNode, distance: int) -> dict:
        
        if root is None:
            return defaultdict(int)

        if root.left is None and root.right is None:
            count = defaultdict(int)
            count[1] = 1
            return count
        
        left_dist = self._dfs(root.left, distance)
        right_dist = self._dfs(root.right, distance)

        for dl in left_dist:
            for dr in right_dist:
                if dl + dr <= distance:
                    self.pairs += left_dist[dl] * right_dist[dr]
        
        all_dist = defaultdict(int)

        for d in left_dist:
            if d + 1 <= distance:
                all_dist[d + 1] = left_dist[d]
        for d in right_dist:
            if d + 1 <= distance:
                all_dist[d + 1] += right_dist[d]
        
        return all_dist
        