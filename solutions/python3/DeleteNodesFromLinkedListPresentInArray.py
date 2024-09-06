# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        nums_set = set(nums)
        dummy = ListNode(0, head)

        temp = dummy
        while temp is not None:
            while temp.next is not None and temp.next.val in nums_set:
                temp.next = temp.next.next
            temp = temp.next
        
        return dummy.next
        
        
        # initial solution: handling head and the rest separately

        # nums_set = set(nums)
        # res = head

        # # head
        # while res is not None and res.val in nums_set:
        #     res = res.next

        # temp = res

        # # rest of element
        # while temp is not None:
        #     while temp.next is not None and temp.next.val in nums_set:
        #         temp.next = temp.next.next
        #     temp = temp.next
        
        # return res
