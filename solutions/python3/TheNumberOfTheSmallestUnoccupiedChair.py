class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        
        times_sorted = times.copy()
        times_sorted.sort()
        
        target_friend = times[targetFriend]

        free_chairs_heap = [i for i in range(len(times))]
        heapq.heapify(free_chairs_heap)
        
        leaving_heap = []
        for arrival, leaving in times_sorted:
            while leaving_heap and leaving_heap[0][0] <= arrival:
                _, _, chair = heapq.heappop(leaving_heap)
                heapq.heappush(free_chairs_heap, chair)
            if [arrival, leaving] == target_friend:
                return free_chairs_heap[0]
            else:
                heapq.heappush(leaving_heap, [leaving, arrival, heapq.heappop(free_chairs_heap)])
            
        return -1   # shouldn't happen
