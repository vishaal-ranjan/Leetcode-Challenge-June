# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.dfs(root)
        return self.count
    
    def dfs(self, root):
        if not root:
            return
        self.count += 1
        if root.left:
            self.dfs(root.left)
        if root.right:
            self.dfs(root.right)