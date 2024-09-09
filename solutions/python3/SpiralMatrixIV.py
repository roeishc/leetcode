# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        top, bottom = 0, m
        left, right = 0, n
        temp = head

        res = [[-1] * n for _ in range(m)]

        while temp:
            
            # left to right
            for i in range(left, right):
                if temp is None:
                    return res
                res[top][i] = temp.val
                temp = temp.next
            top += 1

            # top to bottom
            for i in range(top, bottom):
                if temp is None:
                    return res
                res[i][right - 1] = temp.val
                temp = temp.next
            right -= 1

            # right to left
            for i in range(right - 1, left - 1, -1):
                if temp is None:
                    return res
                res[bottom - 1][i] = temp.val
                temp = temp.next
            bottom -= 1

            # bottom to top
            for i in range(bottom - 1, top - 1, -1):
                if temp is None:
                    return res
                res[i][left] = temp.val
                temp = temp.next
            left += 1

        return res
