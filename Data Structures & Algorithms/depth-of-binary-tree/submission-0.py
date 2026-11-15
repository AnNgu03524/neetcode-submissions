# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# Recursive depth first search

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: node is empty, return 0
        if not root:
            return 0
        
        # At non-empty nodes, recurse on their children as the new root. Each call down is +1 level.
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
        

        
        