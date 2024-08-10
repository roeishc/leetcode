class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        res = []

        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(interval[1], res[-1][1])
        
        return res


        # initial solutions: O(n^2) because removing from list is O(n)

        # n = len(intervals)
        # i = 0
        # res = deepcopy(intervals)

        # while i < n - 1:
        #     while i < n - 1 and res[i][1] >= res[i+1][0]:
        #         res[i][1] = res[i+1][1]
        #         res.remove(res[i+1])
        #         n -= 1
        #     i += 1
        
        # return res
