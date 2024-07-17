# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    forest: List[TreeNode] = []


    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        self.forest = []

        to_delete_set = set(to_delete)

        root = self._helper(root, to_delete_set)

        if root:
            self.forest.append(root)

        return self.forest


    def _helper(self, root: Optional[TreeNode], to_delete: List[int]):
        
        if root is None:
            return None
        
        root.left = self._helper(root.left, to_delete)
        root.right = self._helper(root.right, to_delete)

        if root.val in to_delete:
            if root.left:
                self.forest.append(root.left)
            if root.right:
                self.forest.append(root.right)
            return None # to delete the current node, return None to its parent
        
        return root



# initial solution: works, but clunky code.
# checking for 2 levels down instead of 1 level down.
# bad readability

# class Solution:

#     forest: List[TreeNode] = []


#     def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
#         self.forest = []

#         to_delete_set = set(to_delete)

#         if root.val in to_delete_set:
#             to_delete_set.remove(root.val)
#             if root.left is not None and root.left.val not in to_delete_set:
#                 self.forest.append(root.left)
#             if root.right is not None and root.right.val not in to_delete_set:
#                 self.forest.append(root.right)
#         else:
#             self.forest.append(root)
        
#         self.helper(root, to_delete_set)

#         return self.forest


#     def helper(self, root: Optional[TreeNode], to_delete: List[int]):

#         if root is None or not to_delete:
#             return

#         if root.left is not None:
#             self.helper(root.left, to_delete)
#             if root.left.val in to_delete:
#                 to_delete.remove(root.left.val)
#                 if root.left.right is not None:
#                     self.forest.append(root.left.right)
#                 if root.left.left is not None:
#                     self.forest.append(root.left.left)
#                 root.left = None

#         if root.right is not None:
#             self.helper(root.right, to_delete)
#             if root.right.val in to_delete:
#                 to_delete.remove(root.right.val)
#                 if root.right.right is not None:
#                     self.forest.append(root.right.right)
#                 if root.right.left is not None:
#                     self.forest.append(root.right.left)
#                 root.right = None
