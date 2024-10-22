# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        bfs_order = deque([root])
        min_heap = []   # maintain up to k largest values in a minimum heap

        while bfs_order:
            level_sum = 0
            level_length = len(bfs_order)
            for i in range(level_length):
                cur_node = bfs_order.popleft()
                level_sum += cur_node.val
                if cur_node.left:
                    bfs_order.append(cur_node.left)
                if cur_node.right:
                    bfs_order.append(cur_node.right)
            heapq.heappush(min_heap, level_sum)
            if len(min_heap) > k:   # maintain up to size k in the minimum heap
                heapq.heappop(min_heap)

        return -1 if k > len(min_heap) else min_heap[0]


# solution with sorting the values instead of using a heap:

# class Solution:
#     def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
#         level_sum = defaultdict(int)
#         bfs_order = deque([(root, 1)])

#         while bfs_order:
#             cur_node, cur_level = bfs_order.popleft()
#             level_sum[cur_level] += cur_node.val
#             if cur_node.left:
#                 bfs_order.append((cur_node.left, cur_level + 1))
#             if cur_node.right:
#                 bfs_order.append((cur_node.right, cur_level + 1))

#         if len(level_sum) < k:
#             return -1
        
#         sums_sorted = sorted(level_sum.values(), reverse=True)
#         return sums_sorted[k - 1]
