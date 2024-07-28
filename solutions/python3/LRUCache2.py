class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # maps key to node
        # left=LRU, right=most recently used
        self.left, self.right = Node(0, 0), Node(0, 0)  # dummy nodes to fill left and right before elements
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key in self.cache:   # if it's already in cache, move it to be most recently used before returning
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next    # the `next` of the left-most dummy node holds the LRU node
            self._remove(lru)
            del self.cache[lru.key]

    # helper functions
    def _remove(self, node):
        prev, nextt = node.prev, node.next
        prev.next = nextt
        nextt.prev = prev

    def _insert(self, node):
        prev, nextt = self.right.prev, self.right
        prev.next = nextt.prev = node   # insert node in between right-most and 1 before right-most
        node.prev, node.next = prev, nextt


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)