class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        HashSet<Character> allowedSet = new HashSet();
        for (char c : allowed.toCharArray())
            allowedSet.add(c);

        int res = 0;
        for (String word : words){
            if (isWordConsistent(word, allowedSet))
                res += 1;
        }
        return res;
    }


    public boolean isWordConsistent(String word, HashSet<Character> allowedSet){
        for (char c : word.toCharArray()){
            if (!allowedSet.contains(c))
                return false;
        }
        return true;
    }
}