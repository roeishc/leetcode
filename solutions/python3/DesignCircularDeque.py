class DoublyLinkedListNode:
    def __init__(self, val, nextt=None, prev=None):
        self.val = val
        self.next = nextt
        self.prev = prev


class MyCircularDeque:
    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.total = 0
        self.max = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.head:   # is not None
            new_node = DoublyLinkedListNode(val=value, nextt=self.head)
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = DoublyLinkedListNode(val=value)
            self.tail = self.head
        self.total += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.tail:   # is not None
            new_node = DoublyLinkedListNode(val=value, prev=self.tail)
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = DoublyLinkedListNode(val=value)
            self.head = self.tail
        self.total += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.total == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        self.total -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.total == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
        self.total -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.total == 0

    def isFull(self) -> bool:
        return self.total == self.max


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()