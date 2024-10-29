class Solution {
    public boolean isValid(String s) {
        
        Stack<Character> stack = new Stack<>();
        
        HashMap<Character, Character> matchParentheses = new HashMap<>();
        matchParentheses.put('(', ')');
        matchParentheses.put('[', ']');
        matchParentheses.put('{', '}');

        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if (matchParentheses.containsKey(c))   // if c is an opening bracket
                stack.push(c);
            else {   // c is a closing bracket
                if (stack.size() == 0)
                    return false;
                char lastOpen = stack.pop();
                if (matchParentheses.get(lastOpen) != c)
                    return false;
            }
        }

        return stack.isEmpty();

    }
}