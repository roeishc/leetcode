class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # Min Heap solution:
        min_heap = MinHeap(nums)
        return [min_heap.pop() for _ in range(len(nums))]
        
        # Max Heap solution:
        # negatives = [-num for num in nums]
        # max_heap = MaxHeap(negatives)
        # return [-max_heap.pop() for _ in range(len(negatives))]


class MinHeap:

    def __init__(self, arr: List = None):
        if arr is None:
            self.heap = []
        else:
            self.heap = arr
            self.build_min_heap(arr)

    def push(self, val: int):
        self.heap.append(val)
        self.bubble_up(len(self.heap) - 1)

    def pop(self) -> int:
        if not self.heap:
            raise IndexError("pop from empty heap")
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        res = self.heap.pop()
        if self.heap:
            self.min_heapify(0, len(self.heap))
        return res

    def build_min_heap(self, arr: List):
        # assuming `arr` is a list representation of an almost complete binary tree
        self.heap = arr
        n = len(arr)
        for i in range(n // 2, -1, -1):
            self.min_heapify(i, n)

    def min_heapify(self, idx: int, heap_size: int):

        left = 2 * idx + 1
        right = left + 1

        smallest = idx

        if left < heap_size and self.heap[left] < self.heap[idx]:
            smallest = left

        if right < heap_size and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self.min_heapify(smallest, heap_size)

    def bubble_up(self, idx: int):
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[parent] > self.heap[idx]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = (idx - 1) // 2


class MaxHeap:

    def __init__(self, arr: List = None):
        if arr is None:
            self.heap = []
        else:
            self.heap = arr
            self.build_max_heap(arr)

    def push(self, val: int):
        self.heap.append(val)
        self.bubble_up(len(self.heap) - 1)

    def pop(self) -> int:
        if not self.heap:
            raise IndexError("pop from empty heap")
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        res = self.heap.pop()
        if self.heap:
            self.max_heapify(0)
        return res

    def build_max_heap(self, arr: List):
        n = len(arr)
        for i in range(n // 2, -1, -1):
            self.max_heapify(i)

    def max_heapify(self, idx: int):
        heap_size = len(self.heap)
        left = 2 * idx + 1
        right = left + 1
        largest = idx

        if left < heap_size and self.heap[left] > self.heap[largest]:
            largest = left

        if right < heap_size and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != idx:
            self.heap[largest], self.heap[idx] = self.heap[idx], self.heap[largest]
            self.max_heapify(largest)

    def bubble_up(self, idx: int):
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[idx] > self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = (idx - 1) // 2
