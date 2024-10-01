class CustomStack {

    int max;
    Stack<Integer> stack;

    public CustomStack(int maxSize) {
        max = maxSize;
        stack = new Stack<>();
    }
    
    public void push(int x) {
        if (!isFull())
            stack.add(x);
    }
    
    public int pop() {
        if (stack.isEmpty())
            return -1;
        return stack.pop();
    }
    
    public void increment(int k, int val) {
        int min = Math.min(k, stack.size());
        for (int i = 0; i < min; i++)
            stack.set(i, stack.get(i) + val);
    }

    private boolean isFull(){
        return max == stack.size();
    }

}

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = new CustomStack(maxSize);
 * obj.push(x);
 * int param_2 = obj.pop();
 * obj.increment(k,val);
 */