class Solution:
    def compressedString(self, word: str) -> str:

        res  = []

        cur = None
        count = 0

        for c in word:
            if c == cur:
                count += 1
                if count == 9:
                    res.append(str(count))
                    res.append(c)
                    cur = None
                    count = 0
            else:
                if cur: # is not None...
                    res.append(str(count))
                    res.append(cur)
                cur = c
                count = 1
        
        if cur:
            res.append(str(count))
            res.append(cur)

        return "".join(res)
