class Solution {
    public int[] leftRightDifference(int[] nums) {
        
        int len = nums.length;
        
        int[] leftSum = new int[len];
        leftSum[0] = 0;

        int[] rightSum = new int[len];
        rightSum[len - 1] = 0;

        for (int i = 1; i < len; i++)
            leftSum[i] = leftSum[i - 1] + nums[i - 1];

        for (int i = len - 2; 0 <= i; i--)
            rightSum[i] = rightSum[i + 1] + nums[i + 1];

        int[] answer = new int[len];
        for (int i = 0; i < len; i++)
            answer[i] = Math.abs(leftSum[i] - rightSum[i]);

        return answer;

    }
}