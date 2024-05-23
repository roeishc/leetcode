def count_beautiful_subsets(nums: List[int], k: int, freq_map: dict, i: int):
    
    if i == len(nums):
        return 1

    total_count = count_beautiful_subsets(nums, k, freq_map, i + 1)

    if nums[i] - k not in freq_map:
        freq_map[nums[i]] += 1

        total_count += count_beautiful_subsets(nums, k, freq_map, i + 1)
        freq_map[nums[i]] -= 1

        if freq_map[nums[i]] == 0:
            del freq_map[nums[i]]

    return total_count


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int):
        freq_map = defaultdict(int)
        nums.sort()
        return count_beautiful_subsets(nums, k, freq_map, 0) - 1
