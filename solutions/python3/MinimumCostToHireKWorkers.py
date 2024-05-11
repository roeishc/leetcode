class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted(([w/q, q] for w, q in zip(wage, quality)), key=lambda x: x[0])
        res: float = sys.float_info.max
        quality_sum: float = 0
        max_heap = []
        heap_len: int

        for ratio, w_quality in workers:
            heappush(max_heap, w_quality)
            quality_sum += w_quality
            heap_len = len(max_heap)

            if k < heap_len:
                quality_sum -= heappop(max_heap)
                heap_len -=1
            if k == heap_len:
                res = min(res, ratio * quality_sum)

        return res


def heappush(heap, item):   # max heap push
    return heapq.heappush(heap, -item)


def heappop(heap):  # max heap pop
    return -heapq.heappop(heap)