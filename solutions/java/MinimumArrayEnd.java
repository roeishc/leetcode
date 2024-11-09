class Solution {
    public long minEnd(int n, int x) {
        
        if (n == 1)
            return x;
        
        String xBinary = Integer.toBinaryString(x);
    
        int resSize = 64;   // long type has 8 bytes - 64 bits
        
        int[] bits = new int[resSize];
        for (int i = xBinary.length() - 1, j = resSize - 1; i >= 0; i--, j--)
            bits[j] = xBinary.charAt(i) == '1' ? 1 : 0;

        String nBinary = Integer.toBinaryString(n - 1);

        int i = resSize - 1;
        int j = nBinary.length() - 1;
        while (i >= 0 && j >= 0){
            if (bits[i] == 0)
                bits[i] = nBinary.charAt(j--) == '1' ? 1 : 0;
            i--;
        }

        long res = 0;
        for (i = resSize - 1; i >= 0; i--)
            res |= bits[i] == 1 ? (1L << (resSize - 1 - i)) : 0;

        return res;

    }
}