# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [ float('-inf')]
        def find_max_sum(node):
            if not node:
                return 0 
            
            left = find_max_sum(node.left)
            right  = find_max_sum(node.right)
            res[0] = max(left + node.val , right+node.val , node.val , res[0],left+right+node.val)
            return max(node.val + max(left , right), node.val)
        
        find_max_sum(root)

        return res[0]