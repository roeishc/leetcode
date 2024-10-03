class Solution {
    public int minSubarray(int[] nums, int p) {
        
        long total = Arrays.stream(nums).asLongStream().sum();  // to account for int overflow
        int remainder = (int)(total % p);
        
        if (remainder == 0)
            return 0;

        int res = nums.length;

        HashMap<Integer, Integer> remainderToIdx = new HashMap<>();
        remainderToIdx.put(0, -1);

        int curSumRemainder = 0;
        for (int i = 0; i < nums.length; i++){
            curSumRemainder = (curSumRemainder + nums[i]) % p;
            int prefix = ((curSumRemainder - remainder) + p) % p;
            if (remainderToIdx.containsKey(prefix))
                res = Math.min(res, i - remainderToIdx.get(prefix));
            remainderToIdx.put(curSumRemainder, i);
        }

        return res == nums.length? -1 : res;

    }
}