# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.total = 0
        self.helper(root, '')
        return self.total
    
    def helper(self, root, temp):
        if not root:
            return
        temp += str(root.val)
        if not root.left and not root.right:
            self.total += int(temp)
        self.helper(root.left, temp)
        self.helper(root.right, temp)