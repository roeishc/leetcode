# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        temp = node
        while temp.next != None:
            temp.val = temp.next.val
            if temp.next.next == None:
                temp.next = None
                break
            temp = temp.next
        