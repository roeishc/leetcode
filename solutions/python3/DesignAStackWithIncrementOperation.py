class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.max = maxSize

    def push(self, x: int) -> None:
        if self._is_full():
            return
        self.stack.append(x)
        
    def pop(self) -> int:
        if self._is_empty():
            return -1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val
    
    def _is_full(self):
        return len(self.stack) == self.max
        
    def _is_empty(self):
        return len(self.stack) == 0

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)