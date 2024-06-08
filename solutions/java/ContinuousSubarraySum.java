class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        HashMap<Integer, Integer> modSeen = new HashMap<>();
        modSeen.put(0, -1);
        int prefixMod = 0;
        for (int i = 0; i < nums.length; i++){
            prefixMod = (prefixMod + nums[i]) % k;
            if (modSeen.containsKey(prefixMod)){
                if (1 < i - modSeen.get(prefixMod))
                    return true;
            }
            else
                modSeen.put(prefixMod, i);
        }
        return false;
    }
}