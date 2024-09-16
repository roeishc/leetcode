class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        times_in_seconds = []
        for point in timePoints:
            hours = point[0:2]
            minutes = point[3:5]
            times_in_seconds.append(int(hours) * 60 * 60 + int(minutes) * 60)
        
        n = len(times_in_seconds)
        if n < 2:
            return 0
        
        times_in_seconds.sort()
        res = self.difference(times_in_seconds[0], times_in_seconds[1])
        for i in range(1, n - 1):
            res = min(res, self.difference(times_in_seconds[i], times_in_seconds[i + 1]))
        res = min(res, self.difference(times_in_seconds[0], times_in_seconds[-1]))

        return res // 60
        
    
    def difference(self, time1, time2) -> int:
        # time1 and time2 are in seconds since 00:00
        diff = abs(time1 - time2)
        return min(diff, 86400 - diff)  # 86400 = 24 * 60 * 60 - seconds in a day
        