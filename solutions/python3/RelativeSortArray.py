class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        len1 = 0
        
        # find frequencies of all elements in arr1
        freqs = defaultdict(int)
        for num in arr1:
            freqs[num] += 1
            len1 += 1

        # place all the elements of arr2 into the result array according
        # to their order in arr2 and to their frequencies in arr1 and 
        res = [0] * len1
        i = 0
        for num in arr2:
            while freqs[num] > 0:
                res[i] = num
                freqs[num] -= 1
                i += 1
        
        # now, the elements which aren't in arr2 are the only ones
        # with a positive frequency value in `freqs`
        remaining = []
        for k, v in freqs.items():
            while v > 0:
                remaining.append(k)
                v -= 1
        remaining.sort()

        # populate the rest of the result array with the sorted array
        j = 0
        while i < len1:
            res[i] = remaining[j]
            i += 1
            j += 1

        return res
