class Solution {
    public int heightChecker(int[] heights) {
        int res = 0;
        int[] clone = heights.clone();
        countingSort(clone);
        for (int i = 0; i < heights.length; i++){
            if (heights[i] != clone[i])
                res++;
        }
        return res;
    }

    private void countingSort(int[] arr){
        int maxVal, minVal;
        maxVal = minVal = arr[0];
        HashMap<Integer, Integer> freqs = new HashMap<>();
        for (int num : arr){
            freqs.put(num, freqs.getOrDefault(num, 0) + 1);
            maxVal = Math.max(maxVal, num);
            minVal = Math.min(minVal, num);
        }
        int idx = 0;
        for (int val = minVal; val <= maxVal; val++){
            while (freqs.getOrDefault(val, 0) > 0){
                arr[idx] = val;
                freqs.put(val, freqs.get(val) - 1);
                idx++;
            }
        }
    }
}