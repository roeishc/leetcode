class Solution {
    public boolean canSortArray(int[] nums) {

        int minSegment = nums[0];
        int maxSegment = nums[0];
        int setBits = Integer.bitCount(nums[0]);

        int maxPrevSegment = Integer.MIN_VALUE;
        
        for (int i = 1; i < nums.length; i++){
            if (Integer.bitCount(nums[i]) == setBits){
                minSegment = Math.min(minSegment, nums[i]);
                maxSegment = Math.max(maxSegment, nums[i]);
            }
            else {
                if (minSegment < maxPrevSegment)
                    return false;
                maxPrevSegment = maxSegment;
                maxSegment = minSegment = nums[i];
                setBits = Integer.bitCount(nums[i]);
            }
        }

        if (minSegment < maxPrevSegment)
            return false;
        
        return true;

    }
}