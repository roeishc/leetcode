# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        heights = {}
        results = {}
        
        def height(node):
            if not node:
                return -1
            if node.val in heights:
                return heights[node.val]
            heights[node.val] = 1 + max(height(node.left), height(node.right))
            return heights[node.val]
        
        def dfs(node, cur_height, max_height):
            if not node:
                return
            results[node.val] = max_height
            dfs(
                node.left,
                cur_height + 1,
                max(max_height, cur_height + 1 + height(node.right))
            )
            dfs(
                node.right,
                cur_height + 1,
                max(max_height, cur_height + 1 + height(node.left))
            )

        dfs(root, 0, 0)

        return [results[q] for q in queries]
