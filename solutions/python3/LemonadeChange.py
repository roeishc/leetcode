class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        

        freqs = defaultdict(int)
        for bill in bills:
            if bill == 5:
                freqs[bill] += 1
            elif bill == 10:
                if freqs[5] > 0:    # change of 5
                    freqs[bill] += 1
                    freqs[5] -= 1
                else:
                    return False
            elif bill == 20:
                if freqs[10] > 0 and freqs[5] > 0:  # change of 10 + 5
                    freqs[5] -= 1
                    freqs[10] -= 1
                    freqs[bill] += 1
                elif freqs[5] >= 3: # change of 5 + 5 + 5
                    freqs[5] -= 3
                    freqs[bill] += 1
                else:
                    return False

        return True
