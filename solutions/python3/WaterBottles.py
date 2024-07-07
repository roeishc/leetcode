class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        # explanation:
        # we exchange numExchange EMPTY bottles for 1 FULL bottle.
        # instead, let's look at it the following way:
        # we give away numExchange-1 EMPTY bottles for 1 REFILL of an empty bottle we already have.
        # so let's first drink all of our FULL bottles (numBottles).
        # then, let's place 1 EMPTY bottle aside (thus numBottles -1)
        # now, we can trade numExchange-1 EMPTY bottles for 1 refill (each) of our bottle on the side.
        # MAGICAL
        
        return numBottles + (numBottles - 1) // (numExchange - 1)


        # initial solution: simulating the process

        # res = numBottles

        # while numBottles >= numExchange:
        #     res += numBottles // numExchange
        #     refilled_bottles = numBottles // numExchange
        #     empty_bottles = numBottles % numExchange
        #     numBottles = refilled_bottles + empty_bottles

        # return res
