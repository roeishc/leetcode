class Solution {
    public boolean canArrange(int[] arr, int k) {

        HashMap<Integer, Integer> modCount = new HashMap<>();
        
        for (int num : arr){
            int mod = ((num % k) + k) % k;
            modCount.put(mod, modCount.getOrDefault(mod, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : modCount.entrySet()){
            int mod = entry.getKey();
            int count = entry.getValue();
            if (mod % k != 0 && count != modCount.getOrDefault(k - mod, 0)
                ||
                mod % k == 0 && count % 2 != 0)
                return false;
        }

        return true;

    }
}