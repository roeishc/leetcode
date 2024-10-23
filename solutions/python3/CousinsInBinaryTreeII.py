# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        level_to_sum = defaultdict(int)
        bfs = deque([(root, 0)])

        while bfs:
            cur_node, cur_level = bfs.popleft()
            level_to_sum[cur_level] += cur_node.val
            if cur_node.left:
                bfs.append((cur_node.left, cur_level + 1))
            if cur_node.right:
                bfs.append((cur_node.right, cur_level + 1))

        bfs.append((root, 0))
        while bfs:
            cur_node, cur_level = bfs.popleft()
            children = 0
            if cur_node.left:
                children += cur_node.left.val
                bfs.append((cur_node.left, cur_level + 1))
            if cur_node.right:
                children += cur_node.right.val
                bfs.append((cur_node.right, cur_level + 1))
            if (cur_level + 1) in level_to_sum:
                if cur_node.left:
                    cur_node.left.val = level_to_sum[cur_level + 1] - children
                if cur_node.right:
                    cur_node.right.val = level_to_sum[cur_level + 1] - children

        root.val = 0
            
        return root
