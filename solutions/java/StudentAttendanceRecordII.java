class Solution {

    private final int MOD = 1000000007;

    private int[][][] memo;

    public int checkRecord(int n) {
        
        memo = new int[n+1][2][3];  // 2 for both options of A, 3 for 0/1/2 L's
        for (int[][] arr2D : memo){
            for (int[] arr1D : arr2D)
                Arrays.fill(arr1D, -1);
        }

        return eligibleCombinations(n, 0, 0);

    }

    private int eligibleCombinations(int n, int totalAbsences, int consecutiveLates){
        
        if (1 < totalAbsences || 2 < consecutiveLates)
            return 0;

        if (n == 0)
            return 1;
        
        if (memo[n][totalAbsences][consecutiveLates] != -1)
            return memo[n][totalAbsences][consecutiveLates];

        int count;
        count = eligibleCombinations(n - 1, totalAbsences, 0) % MOD; // chose P
        count = (count + eligibleCombinations(n - 1, totalAbsences + 1, 0)) % MOD; // chose A
        count = (count + eligibleCombinations(n - 1, totalAbsences, consecutiveLates + 1)) % MOD; // chose L

        return memo[n][totalAbsences][consecutiveLates] = count;

    }

}