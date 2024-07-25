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

    def __int__(self):
        self.heap = []

    def __init__(self, arr: List):
        self.heap = None
        self.build_min_heap(arr)

    def push(self, val: int):
        self.heap.append(val)
        self.min_heapify(0, len(self.heap))

    def pop(self) -> int:
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        res = self.heap.pop()
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


class MaxHeap:

    def __int__(self):
        self.heap = []

    def __init__(self, arr: List):
        self.heap = None
        self.build_max_heap(arr)

    def push(self, val: int):
        self.heap.append(val)
        self.max_heapify(0, len(self.heap))

    def pop(self) -> int:
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        res = self.heap.pop()
        self.max_heapify(0, len(self.heap))
        return res

    def build_max_heap(self, arr: List):
        # assuming `arr` is a list representation of an almost complete binary tree
        self.heap = arr
        n = len(arr)
        for i in range(len(arr) // 2, -1, -1):
            self.max_heapify(i, n)

    def max_heapify(self, idx: int, heap_size: int):

        left = 2 * idx + 1
        right = left + 1

        largest = idx

        if left < heap_size and self.heap[idx] < self.heap[left]:
            largest = left

        if right < heap_size and self.heap[largest] < self.heap[right]:
            largest = right

        if largest != idx:
            self.heap[largest], self.heap[idx] = self.heap[idx], self.heap[largest]
            self.max_heapify(largest, heap_size)
