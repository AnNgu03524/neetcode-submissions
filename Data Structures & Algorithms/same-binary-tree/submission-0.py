# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base cases: empty trees / hitting leaf
        if (p == None) and (q == None): # Both are empty
            return True
        elif (p == None) or (q == None): # Either both not both are empty
            return False

        # Base case: Compare roots
        if p.val == q.val:
            # Begin recursing down sub-trees
            leftTreesMatch = self.isSameTree(p.left, q.left)
            rightTreesMatch = self.isSameTree(p.right,q.right)
            return leftTreesMatch and rightTreesMatch
        else:
            return False


        
        