# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        nodes = {}
        children = set()

        for d in descriptions:
            if d[0] not in nodes:
                nodes[d[0]] = TreeNode(d[0])
            if d[2] == 1:   # left child
                if d[1] not in nodes:
                    nodes[d[0]].left = TreeNode(d[1])
                    nodes[d[1]] = nodes[d[0]].left
                else:
                    nodes[d[0]].left = nodes[d[1]]
            else:           # right child
                if d[1] not in nodes:
                    nodes[d[0]].right = TreeNode(d[1])
                    nodes[d[1]] = nodes[d[0]].right
                else:
                    nodes[d[0]].right = nodes[d[1]]
            children.add(d[1])

        # find root
        for d in descriptions:
            if d[0] not in children:
                return nodes[d[0]]

        return None
        