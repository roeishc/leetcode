# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head
        while temp and temp.next:
            gcd = self._get_gcd(temp.val, temp.next.val)
            new_node = ListNode(gcd)
            new_node.next = temp.next
            temp.next = new_node
            temp = new_node.next
        
        return head


    def _get_gcd(self, x: int, y: int) -> int:
        while y:
            x, y = y, x % y
        return abs(x)
        