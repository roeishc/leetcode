class Solution:
    def minimumPushes(self, word: str) -> int:
        
        freqs = Counter(word)
        max_heap = [(-freq, letter) for letter, freq in freqs.items()]
        heapq.heapify(max_heap)

        res, col = 0, 1
        while max_heap:
            for _ in range(8):
                if max_heap:
                    freq, letter = heapq.heappop(max_heap)
                    freq = -freq
                    res += freq * col
            col += 1
        
        return res
