"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        if root is None:
            return []
        
        stack = [root]
        res = []

        while stack:
            cur = stack.pop()
            res.append(cur.val)
            for c in cur.children:
                stack.append(c)
        
        res.reverse()
        return res


        # recursive solution:
        
        # res = []
        
        # def helper(node):
        #     if node is None:
        #         return
        #     for n in node.children:
        #         helper(n)
        #     res.append(node.val)
        
        # helper(root)
        # return res
