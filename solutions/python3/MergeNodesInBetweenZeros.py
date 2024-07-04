# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        new_head = head.next
        temp = new_head

        while temp is not None:
            if temp.val != 0:
                prev = self.get_total_node(temp)
            else:
                prev.next = temp.next
            temp = temp.next

        return new_head


    def get_total_node(self, head: Optional[ListNode]):
        temp = head
        total = 0
        while temp is not None and temp.val != 0:
            total += temp.val
            temp = temp.next
        head.val = total
        head.next = temp
        return head
