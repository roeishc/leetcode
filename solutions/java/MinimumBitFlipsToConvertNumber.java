class Solution {
    public int minBitFlips(int start, int goal) {
        
        String startBinaryString = Integer.toBinaryString(start);
        String goalBinaryString = Integer.toBinaryString(goal);

        int maxLen = Math.max(startBinaryString.length(), goalBinaryString.length());

        // padding the shorter string with 0s so their legnths match
        startBinaryString = Integer.toBinaryString((1 << maxLen) | start).substring(1);
        goalBinaryString = Integer.toBinaryString((1 << maxLen) | goal).substring(1);

        int res = 0;
        for (int i = 0; i < maxLen; i++)
            res += startBinaryString.charAt(i) == goalBinaryString.charAt(i) ? 0 : 1;

        return res;

    }
}