# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    sorted_vals = []

    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.sorted_vals = []
        self.inorder(root)
        return self.build_tree(0, len(self.sorted_vals) - 1)

    
    def inorder(self, root: TreeNode):
        if root is None:
            return
        self.inorder(root.left)
        self.sorted_vals.append(root.val)
        self.inorder(root.right)
    
    
    def build_tree(self, start: int, end: int) -> TreeNode:
        if end < start:
            return None
        
        mid = start + (end - start) // 2

        left = self.build_tree(start, mid - 1)
        right = self.build_tree(mid + 1, end)

        return TreeNode(self.sorted_vals[mid], left, right)