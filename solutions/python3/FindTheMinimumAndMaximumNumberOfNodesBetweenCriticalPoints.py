# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        if head is None or head.next is None or head.next.next is None:
            return [-1, -1]

        prev = head
        cur = head.next

        crits = []
        i = 1

        while cur.next is not None:
            if cur.val < prev.val and cur.val < cur.next.val or cur.val > prev.val and cur.val > cur.next.val:
                crits.append(i)
            cur = cur.next
            prev = prev.next
            i += 1
            
        if len(crits) < 2:
            return [-1, -1]

        min_dist = float('inf')
        for i in range(1, len(crits)):
            min_dist = min(min_dist, crits[i] - crits[i - 1])

        return [min_dist, crits[-1] - crits[0]]
