class Solution {
    public long dividePlayers(int[] skill) {
        
        double targetDouble = (double)Arrays.stream(skill).sum() / skill.length * 2;

        if (targetDouble != (int)targetDouble)
            return -1;

        int target = (int)targetDouble;

        HashMap<Integer, Integer> count = new HashMap<>();
        for (int num : skill)
            count.put(num, count.getOrDefault(num, 0) + 1);

        long res = 0;
        for (Map.Entry<Integer, Integer> entry : count.entrySet()){
            int key = entry.getKey();
            int value = entry.getValue();
            if (value != count.getOrDefault(target - key, 0))
                return -1;
            res += (long)key * (target - key) * value;
        }

        return res / 2;

    }
}