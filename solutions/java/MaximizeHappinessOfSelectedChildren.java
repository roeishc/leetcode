class Solution {
    public long maximumHappinessSum(int[] happiness, int k) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        long res = 0;
        int temp;
        for (int num : happiness) // creating the stack: O(n)
            maxHeap.add(num);
        for (int i = 0; i < k; i++){ // removing k (largest) elements: O(k * logn)
            temp = maxHeap.remove();
            res += Math.max(temp - i, 0);
        }
        return res;
    }
}