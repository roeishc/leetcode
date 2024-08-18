class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        nums = [1]
        i2 = i3 = i5 = 0
        
        for i in range(1, n):
            next_num = min(
                nums[i2] * 2,
                nums[i3] * 3,
                nums[i5] * 5
            )
            nums.append(next_num)
            if next_num == nums[i2] * 2:
                i2 += 1
            if next_num == nums[i3] * 3:
                i3 += 1
            if next_num == nums[i5] * 5:
                i5 += 1
        
        return nums[n - 1]


        # heap solution: O(nlogn)
        
        # min_heap = [1]
        # seen = set()
        # i = 0

        # while i < n:
        #     cur = heapq.heappop(min_heap)
        #     if cur in seen:
        #         continue
        #     heapq.heappush(min_heap, cur * 2)
        #     heapq.heappush(min_heap, cur * 3)
        #     heapq.heappush(min_heap, cur * 5)
        #     seen.add(cur)
        #     i += 1
        
        # return cur
