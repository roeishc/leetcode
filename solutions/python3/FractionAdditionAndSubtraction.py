class Solution:
    def fractionAddition(self, expression: str) -> str:
        
        total_numerator = 0
        total_denominator = 1

        nums = re.split("/|(?=[-+])", expression)
        print(nums)
        nums = list(filter(None, nums))
        print(nums)

        for i in range(0, len(nums), 2):
            current_numerator = int(nums[i])
            current_denominator = int(nums[i + 1])

            total_numerator = total_numerator * current_denominator + current_numerator * total_denominator
            total_denominator *= current_denominator
        
        gcd = abs(self._find_gcd(total_numerator, total_denominator))

        total_numerator //= gcd
        total_denominator //= gcd

        return str(total_numerator) + "/" + str(total_denominator)


    def _find_gcd(self, a: int, b: int) -> int:
        if a == 0:
            return b
        return self._find_gcd(b % a, a)
        