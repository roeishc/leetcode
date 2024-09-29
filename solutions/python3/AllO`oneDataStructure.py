class Node:
    def __init__(self, freq: int):
        self.freq = freq
        self.prev = None
        self.next = None
        self.keys = set()


class AllOne:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_to_node = {}

    def inc(self, key: str) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            freq = node.freq
            node.keys.remove(key)
            next_node = node.next
            if next_node == self.tail or next_node.freq != freq + 1:
                new_node = Node(freq + 1)
                node.next = new_node
                new_node.prev = node
                new_node.next = next_node
                next_node.prev = new_node
                new_node.keys.add(key)
                self.key_to_node[key] = new_node
            else:
                next_node.keys.add(key)
                self.key_to_node[key] = next_node
            if not node.keys:   # if no keys left in current node (because we incremeneted and moved the key to the next node)
                self._remove_node(node)
        else:
            first_node = self.head.next
            if first_node == self.tail or first_node.freq > 1:
                new_node = Node(1)
                self.head.next = new_node
                new_node.prev = self.head
                new_node.next = first_node
                first_node.prev = new_node
                new_node.keys.add(key)
                self.key_to_node[key] = new_node
            else:
                first_node.keys.add(key)
                self.key_to_node[key] = first_node

    def dec(self, key: str) -> None:
        if key not in self.key_to_node:
            return
        
        node = self.key_to_node[key]
        freq = node.freq
        node.keys.remove(key)

        if freq == 1:
            del self.key_to_node[key]
        else:
            prev_node = node.prev
            if prev_node == self.head or prev_node.freq != freq - 1:
                new_node = Node(freq - 1)
                prev_node.next = new_node
                new_node.prev = prev_node
                new_node.next = node
                node.prev = new_node
                new_node.keys.add(key)
                self.key_to_node[key] = new_node
            else:
                prev_node.keys.add(key)
                self.key_to_node[key] = prev_node
        
        if not node.keys:   # no keys left in this node -> remove it
            self._remove_node(node)

    def getMaxKey(self) -> str:
        if self.head.next == self.tail: # if empty
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail: # if empty
            return ""
        return next(iter(self.head.next.keys))

    def _remove_node(self, node: Node):
        prev = node.prev
        nextt = node.next
        prev.next = nextt
        nextt.prev = prev
        

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()