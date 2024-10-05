class Solution {
    public boolean checkInclusion(String s1, String s2) {
        
        if (s2.length() < s1.length())
            return false;

        int[] s1Count = new int[26];
        for (int i = 0; i < s1.length(); i++)
            s1Count[s1.charAt(i) - 'a']++;
        
        int[] windowCount = new int[26];  // count of each English letter in the window
        int left = 0, right = 0;

        while (right < s2.length()) {
            while (right - left < s1.length()) {
                windowCount[s2.charAt(right) - 'a']++;
                right++;
            }
            if (Arrays.equals(s1Count, windowCount))
                return true;
            windowCount[s2.charAt(left) - 'a']--;
            left++;
        }

        return false;

    }
}