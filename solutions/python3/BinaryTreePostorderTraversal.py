# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        stack = [root]
        res = []

        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.left is not None:
                stack.append(cur.left)
            if cur.right is not None:
                stack.append(cur.right)
            
        return res[::-1]


        # recursion solution:

        # res = []

        # def post_order(node):
        #     if node is None:
        #         return
        #     if node.left is not None:
        #         post_order(node.left)
        #     if node.right is not None:            
        #         post_order(node.right)
        #     res.append(node.val)

        # post_order(root)        
        # return res
