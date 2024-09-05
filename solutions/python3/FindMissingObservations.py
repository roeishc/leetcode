class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:

        '''
        assuming we can populate the result with the same roll (assume x), we get:
        (n * x + sum(rolls)) / (n + m) = mean
        
        isolate x:
        x = (mean * (n + m) - sum(rolls)) / n
        
        if x isn't in range [1, 6], we can't populate the reuslt according to the problem's requirements.
        if x is an integer, the result is [x, x, ... , x] (n times).
        if x isn't a whole number but is in the range [1, 6], the remainder of dividing x by n will
        tell us how many elements will be floor(x), and how many will be ceil(x) in the reuslt.
        '''

        m = len(rolls)
        x = (mean * (n + m) - sum(rolls)) / n
        
        if x < 1 or x > 6:
            return []
        
        if x == int(x):
            return [x] * n
        
        x_floor = int(x)
        remainder = x - x_floor

        total_smaller = round(n * (1 - remainder))
        total_larger = round(n * remainder)
        
        return [x_floor] * total_smaller + [x_floor + 1] * total_larger
        # same result
        # return [x_floor if i < total_smaller else x_floor + 1 for i in range(n)]
        