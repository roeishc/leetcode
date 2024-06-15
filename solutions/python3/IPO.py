class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        n = len(profits)
        projects = sorted(zip(capital, profits), key=lambda x: x[0])
        available_projects = []
        i = 0
        
        for _ in range(k):
            # push into the heap all the projects we can afford now
            while i < n and projects[i][0] <= w:
                heapq.heappush(available_projects, -projects[i][1])
                i += 1

            # take the maximum profits project
            if available_projects:  # is not empty...
                w -= heapq.heappop(available_projects)

        return w
