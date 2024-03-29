# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        lst=self.recursion(root)
        return lst[k-1]



    def recursion(self, root):
        if not root:
            return []
        return self.recursion(root.left)+[root.val]+self.recursion(root.right)
