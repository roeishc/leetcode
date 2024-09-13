class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        n = len(arr)
        prefix_xor = [0] * (n + 1)
        for i in range(n):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]

        return [prefix_xor[left] ^ prefix_xor[right + 1] for left, right in queries]
        
        
        # first iteration of the solution: calculate xor of each subarray - O(n * q)
        
    #     res = []
    #     cache = {}
        
    #     for left, right in queries:
    #         if (left, right) in cache:
    #             res.append(cache[(left, right)])
    #         else:
    #             cache[(left, right)] = self.xor_arr(arr[left:right + 1])
    #             res.append(cache[(left, right)])
        
    #     return res


    # def xor_arr(self, arr: List[int]) -> int:
    #     n = len(arr)
    #     if n == 1:
    #         return arr[0]
    #     res = arr[0] ^ arr[1]
    #     if n == 2:
    #         return res
    #     for i in range(2, n):
    #         res ^= arr[i]
    #     return res
