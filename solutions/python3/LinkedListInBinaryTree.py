# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        if self.match_tree_to_ll(root, head):
            return True
        
        if root is None:
            return False
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


    def match_tree_to_ll(self, tree_node, list_node):
        if list_node is None:
            return True
        if tree_node is None or tree_node.val != list_node.val:
            return False
        return self.match_tree_to_ll(tree_node.right, list_node.next) or self.match_tree_to_ll(tree_node.left, list_node.next)

        
        # first iteration: 61/67 passed
        
        # if head is None or root is None:
        #     return False
        
        # if head.val == root.val:
        #     if head.next == None:
        #         return True
        #     print(head.val)
        #     # res_left = self.isSubPath(head.next, root.left)
        #     # res_right = self.isSubPath(head.next, root.right)
        #     return self.isSubPath(head.next, root.left) or self.isSubPath(head.next, root.right)
        
        # return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
        