class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self:
            self.move_to_end(key)
            return self[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)
        self.move_to_end(key)


# solution with an `OrderedDict`` instance in `LRUCache`:

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.d = OrderedDict()

#     def get(self, key: int) -> int:
#         if key in self.d:
#             self.d.move_to_end(key)
#             return self.d[key]
#         else:
#             return -1

#     def put(self, key: int, value: int) -> None:
#         self.d[key] = value
#         if len(self.d) > self.capacity:
#             self.d.popitem(last=False)
#         self.d.move_to_end(key)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)