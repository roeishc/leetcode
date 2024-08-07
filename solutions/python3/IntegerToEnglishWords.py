class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        res = ""
        group_index = 0

        while num > 0:

            if num % 1000 != 0:
                group_res = ""
                part = num % 1000

                if part >= 100:
                    group_res += ones[part // 100] + " Hundred "
                    part %= 100

                if part >= 20:
                    group_res += tens[part // 10] + " "
                    part %= 10
                
                if part > 0:
                    group_res += ones[part] + " "
                
                group_res += thousands[group_index] + " "
                res = group_res + res
            
            num //= 1000
            group_index += 1
        
        return res.strip()
