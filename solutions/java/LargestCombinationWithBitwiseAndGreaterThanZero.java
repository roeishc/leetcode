class Solution {
    public int largestCombination(int[] candidates) {
    

        /* 
            check each bit: 0000 0001
                            0000 0010
                            0000 0100
                            0000 1000
                            0001 0000
                            0010 0000
                            0100 0000
                            1000 0000
            how many numbers in candidates have this bit turned on. return the maximum
            slight optimization: find the maximum bit that's turned on (1) instead of iterating on all 32bits
        */

        int maxVal = Arrays.stream(candidates).max().getAsInt();
        int maxBit = Integer.SIZE - Integer.numberOfLeadingZeros(maxVal);

        int res = 0;
        for (int bit = 0; bit < maxBit; bit++){
            int toCompare = 1 << bit;
            int count = 0;
            for (int num : candidates){
                if ((toCompare & num) != 0)
                    count += 1;
            }
            res = Math.max(res, count);
        }

        return res;

    }
}