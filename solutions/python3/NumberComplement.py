class Solution:
    def findComplement(self, num: int) -> int:
        
        if num == 1:
            return 0
        
        log_res = math.log2(num)
        
        if log_res.is_integer():
            return (1 << int(log_res)) - 1
        
        all_1s = (1 << (math.ceil(log_res))) - 1
        
        return num ^ all_1s
