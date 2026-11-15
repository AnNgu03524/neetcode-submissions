# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# Iterative BFS

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Handle the base case of empty root again
        if not root:
            return 0
        
        # Keep a deque of the current level nodes
        q = deque()
        if root:
            q.append(root)
        
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()  # pop node off queue to acccess its children
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

        
        