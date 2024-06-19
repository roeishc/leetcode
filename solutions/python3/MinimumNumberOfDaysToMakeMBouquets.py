class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if len(bloomDay) < m * k:
            return -1

        start = 0
        end = max(bloomDay)
        res = -1

        while start <= end:
            mid = (start + end) // 2
            b = self.get_num_of_bouquets(bloomDay, k, mid)
            if b < m:
                start = mid + 1
            else:
                res = mid
                end = mid - 1

        return res


    def get_num_of_bouquets(self, bloomDay: List[int], k: int, up_to_day: int) -> int:
        count = 0
        total = 0

        for day in bloomDay:
            if day <= up_to_day:
                count += 1
            else:
                count = 0
            if count == k:
                total += 1
                count = 0
        
        return total