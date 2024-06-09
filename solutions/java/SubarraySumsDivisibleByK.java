class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        int res = 0, prefixMod = 0;
        HashMap<Integer, Integer> seenMod = new HashMap<>();
        seenMod.put(0, 1);
        for (int num : nums){
            prefixMod = ((prefixMod + num) % k + k) % k;    // apply mod k twice for negative mod results
            res += seenMod.getOrDefault(prefixMod, 0);
            seenMod.put(prefixMod, seenMod.getOrDefault(prefixMod, 0) + 1);
        }
        return res;
    }
}