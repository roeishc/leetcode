class Solution {
    public int minPartitions(String n) {
        int max, strLen;
        max = 0;
        strLen = n.length();
        for (int i = 0; i < strLen; i++){
            max = max < n.charAt(i) - '0' ? n.charAt(i) - '0' : max;
            // max = Math.max(max, Character.getNumericValue(n.charAt(i)));     // slower
        }
        return max;
    }
}