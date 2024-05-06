class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:

        enc_len = len(encoded)
        
        arr = [0] * (enc_len + 1)
        arr[0] = first

        i = 1
        for num in encoded:
            arr[i] = arr[i-1] ^ num
            i += 1
        
        return arr

        