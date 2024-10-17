class Solution:
    def maximumSwap(self, num: int) -> int:

        digits = list(map(int, str(num)))
        digits_indexes = defaultdict(list)

        for i, digit in enumerate(digits):
            digits_indexes[digit].append(i)

        digits_sorted = [n for n in digits]
        digits_sorted.sort(reverse=True)

        # the gist: find the first digit which isn't in its place in the descending-order of digits, and replace
        # its LAST occurence (greatest index) with the current position (i)
        for i, digit in enumerate(digits):
            if digit != digits_sorted[i]:
                digits[i], digits[digits_indexes[digits_sorted[i]][-1]] = digits[digits_indexes[digits_sorted[i]][-1]], digits[i]
                break
        
        return int("".join([str(n) for n in digits]))
