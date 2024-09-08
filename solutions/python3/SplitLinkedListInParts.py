# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        ll_len = self._get_linked_list_length(head)
        res = []

        if ll_len <= k:
            temp = head
            i = 0
            while temp is not None:
                res.append(ListNode(temp.val))
                temp = temp.next
                i += 1
            while i < k:
                res.append(None)
                i += 1
            return res

        linked_lists_in_res = ll_len / k
        remainder = linked_lists_in_res - int(linked_lists_in_res)
        
        longer_lists_amount = round(remainder * k)
        longer_lists_len = ceil(linked_lists_in_res)
        
        shorter_lists_amount = round((1 - remainder) * k)
        shorter_lists_len = floor(linked_lists_in_res)

        temp = head
        for _ in range(longer_lists_amount):
            res.append(self._get_first_k(temp, longer_lists_len))
            temp = self._get_tail_after_k(temp, longer_lists_len)
        
        for _ in range(shorter_lists_amount):
            res.append(self._get_first_k(temp, shorter_lists_len))
            temp = self._get_tail_after_k(temp, shorter_lists_len)

        return res


    def _get_linked_list_length(self, head: Optional[ListNode]) -> int:
        res = 0
        temp = head
        while temp is not None:
            res += 1
            temp = temp.next
        return res


    def _get_tail_after_k(self, head, k):
        temp = head
        i = 0
        while temp is not None and i < k:
            temp = temp.next
            i += 1
        return temp

    
    def _get_first_k(self, head, k):
        temp = head
        res = ListNode(0)   # dummy node
        itr = res
        i = 0
        while temp is not None and i < k:
            itr.next = ListNode(temp.val)
            i += 1
            temp = temp.next
            itr = itr.next
        return res.next
