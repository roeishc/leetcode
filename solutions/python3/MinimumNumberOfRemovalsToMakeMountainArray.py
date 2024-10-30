class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        
        N = len(nums)

        lis = [1] * N
        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i], lis[j] + 1)

        lds = [1] * N
        for i in reversed(range(N)):
            for j in range(i + 1, N):
                if nums[j] < nums[i]:
                    lds[i] = max(lds[i], lds[j] + 1)
        
        res = N
        for i in range(1, N - 1):
            if min(lis[i], lds[i]) > 1:
                res = min(
                    res,
                    N - lis[i] - lds[i] + 1
                )

        return res
