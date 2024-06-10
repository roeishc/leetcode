def counting_sort(arr: List[int]):
    freqs = defaultdict(int)
    max_val = min_val = arr[0]
    for num in arr:
        freqs[num] += 1
        if max_val < num:
            max_val = num
        if num < min_val:
            min_val = num
    idx = 0
    for val in range(min_val, max_val + 1):
        while freqs.get(val, 0) > 0:
            arr[idx] = val
            freqs[val] -= 1
            idx += 1


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp = deepcopy(heights)
        # temp.sort()
        counting_sort(temp)
        res = 0
        for i in range(len(heights)):
            if heights[i] != temp[i]:
                res += 1
        return res
        