class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        # iterative solution: O(n) time, O(1) space.
        # relies on turning the recursive solution (below) to iterative

        res = 0

        for people in range(1, n + 1):
            res = (res + k) % people

        return res + 1

        # #############################################################
        # recursive solution: O(n) time, O(n) space

        # def helper(n ,k):
        #     if n == 1:
        #         return 0
        #     return (helper(n - 1, k) + k) % n
        
        # return helper(n, k) + 1
        
        # #############################################################
        # Deque solution: O(n*k)
        
        # deq = deque([i for i in range(1, n + 1)])

        # while len(deq) > 1:
        #     for _ in range(k - 1):
        #         deq.append(deq.popleft())
        #     deq.popleft()
        
        # return deq[0]
        
        # #############################################################
        # initial solution: O(n^2)
        
        # nlist = [i for i in range(n)]
        # i = 0

        # while len(nlist) > 1:
        #     i = (i + k - 1) % len(nlist)
        #     nlist.remove(nlist[i])

        # return nlist[0] + 1
