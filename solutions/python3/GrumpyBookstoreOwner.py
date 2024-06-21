class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        n = len(customers)
        base = 0

        # add all satisfied customers to base (where grumpy[i] == 0)
        for i in range(n):
            base += customers[i] * (grumpy[i] ^ 1)
        
        # initialize max_contribution to the first window in the customers array
        max_contribution = 0
        for i in range(minutes):
            max_contribution += grumpy[i] * customers[i]
        
        # find the largest contribution of grumpy to base in the rest of the customers array
        contribution = max_contribution
        for i in range(minutes, n):
            contribution += grumpy[i] * customers[i]    # add next element to window
            contribution -= grumpy[i - minutes] * customers[i - minutes]    # remove last element from window
            max_contribution = max(max_contribution, contribution)

        return base + max_contribution

        
        # The solution below is O(n*minutes) which is inefficient, but was the first iteration of my solution
        
        # n = len(customers)
        # base = 0

        # for i in range(n):
        #     if grumpy[i] == 0:
        #         base += customers[i]
        
        # # find where the minutes-window has the largest contribution to base
        # max_contribution = 0
        # for i in range(n - minutes + 1):
        #     contribution = 0
        #     sub = customers[i : i + minutes]
        #     sub_g = grumpy[i : i + minutes]
        #     for val, g in zip(sub, sub_g):
        #         if g == 1:
        #             contribution += val
        #     max_contribution = max(max_contribution, contribution)
        
        # return base + max_contribution