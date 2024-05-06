class Solution:
    def numberOfSteps(self, num: int) -> int:
        binary_rep = str(bin(num))[2::]
        return binary_rep.count("0") + 2 * binary_rep.count("1") - 1
            