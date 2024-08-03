class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        return Counter(arr) == Counter(target)
        
        
        # initiail solution: manual counting of elements in each array

        # freqs_arr = defaultdict(int)
        # freqs_target = defaultdict(int)
        
        # for num_arr, num_target in zip(arr, target):
        #     freqs_arr[num_arr] += 1
        #     freqs_target[num_target] += 1
        
        # for val, freq in freqs_arr.items():
        #     if freqs_target[val] != freq:
        #         return False
        
        # return True
