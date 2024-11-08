class Solution {
    public int[] getMaximumXor(int[] nums, int maximumBit) {
        
        int targetVal = (1 << maximumBit) - 1;
        
        int[] prefixXor = new int[nums.length];
        prefixXor[0] = nums[0];
        for (int i = 1; i < prefixXor.length; i++)
            prefixXor[i] = prefixXor[i - 1] ^ nums[i];

        int[] res = new int[nums.length];
        for (int i = 0; i < res.length; i++)
            res[i] = prefixXor[prefixXor.length - 1 - i] ^ targetVal;
        
        return res;
        
    }
}