class Solution {
    public List<String> commonChars(String[] words) {
        
        // using the shortest word for optimization. any word can be used here
        HashMap<String, Integer> w = getWordMap(getShortestWordInList(words));
        HashMap<String, Integer> tempWord;
        
        for (String word : words){
            tempWord = getWordMap(word);
            for (String k : w.keySet()){
                w.put(k, Math.min(
                    w.getOrDefault(k, 0),
                    tempWord.getOrDefault(k, 0)
                ));
            }
        }

        List<String> res = new ArrayList<>();
        Iterator<Map.Entry<String, Integer>> it = w.entrySet().iterator();
        Map.Entry<String, Integer> pair;
        while (it.hasNext()){
            pair = it.next();
            for (int i = 0; i < pair.getValue(); i++)
                res.add(pair.getKey());
        }

        return res;
    }

    private HashMap<String, Integer> getWordMap(String word){
        String temp;
        int freq;
        HashMap<String, Integer> map = new HashMap<>();

        for (int i = 0; i < word.length(); i++){
            temp = String.valueOf(word.charAt(i));
            freq = map.getOrDefault(temp, 0);
            map.put(temp, freq + 1);
        }

        return map;
    }

    private String getShortestWordInList(String[] words){
        String minWord = words[0];
        for (String word : words){
            if (word.length() < minWord.length())
                minWord = word;
        }
        return minWord;
    }
}