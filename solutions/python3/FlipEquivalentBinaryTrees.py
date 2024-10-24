# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        if not root1 and not root2:
            return True
            
        if not root1 or not root2:
            return False            
        
        dq1, dq2 = deque([root1]), deque([root2])

        while dq1 and dq2:
            if len(dq1) != len(dq2):
                return False
            level1, level2 = {}, {}
            for _ in range(len(dq1)):
                node1, node2 = dq1.popleft(), dq2.popleft()
                level1[node1.val], level2[node2.val] = set(), set()
                if node1.left:
                    dq1.append(node1.left)
                    level1[node1.val].add(node1.left.val)
                if node1.right:
                    dq1.append(node1.right)
                    level1[node1.val].add(node1.right.val)
                if node2.left:
                    dq2.append(node2.left)
                    level2[node2.val].add(node2.left.val)
                if node2.right:
                    dq2.append(node2.right)
                    level2[node2.val].add(node2.right.val)
            if level1 != level2:
                return False
            
        return True
