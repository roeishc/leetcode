# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    suffix_sum = []
    i = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        self.suffix_sum = [0]   # apparently, leetcode re-uses the class instance of Solution
        self.i = 0              # between test cases, so restarting is necessary

        self.dfs_suffix_sum(root)

        return root

    def dfs_suffix_sum(self, root: TreeNode) -> None:
        if root is None:
            return
        self.dfs_suffix_sum(root.right)
        self.suffix_sum.append(self.suffix_sum[-1] + root.val)
        root.val = self.suffix_sum[-1]
        self.dfs_suffix_sum(root.left)
