class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # bfs, but allow visitng each node up to 2 times, and remember the visit time of each
        # only allow a second visit if it happens in a later time than the first
        q = deque([1])
        cur_time = 0
        res = -1
        visit_times = defaultdict(list) # node -> [distinct visit times], maximum length of 2 (visiting a node twice with different length paths)

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node == n:
                    if res != -1:   # allow visiting the last node twice to find 2nd shortest path
                        return cur_time
                    res = cur_time
                for nei in adj[node]:
                    if not visit_times[nei] or (len(visit_times[nei]) == 1 and visit_times[nei][0] != cur_time):
                        # only append when we either:
                        #   didn't visit this neighbor yet, or
                        #   visited this neighbor in a prior time, but only once
                        # this is meant to allow the second visit to the destination node in case there's isn't a direct, second, shortest path
                        q.append(nei)
                        visit_times[nei].append(cur_time)
            if (cur_time // change) % 2 == 1:   # need to wait for green signal
                cur_time += change - (cur_time % change)
            cur_time += time    # can now advance

        return -1   # should never happen according to the questions' constraints
