class Solution {
    public int[] arrayRankTransform(int[] arr) {

        if (arr.length == 0)
            return new int[0];
        
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for (int num : arr)
            minHeap.add(num);

        HashMap<Integer, Integer> numToRank = new HashMap<>();

        int rank = 1;
        int prev = minHeap.remove();
        numToRank.put(prev, rank);
        while (!minHeap.isEmpty()){
            int cur = minHeap.remove();
            if (cur > prev)
                rank++;
            numToRank.put(cur, rank);
            prev = cur;
        }

        int res[] = new int[arr.length];
        for (int i = 0; i < arr.length; i++)
            res[i] = numToRank.get(arr[i]);
        
        return res;

    }
}