# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res=[]
        
        def dfs(node,so_far):
            if not node.left and not node.right:
                # print('got here')

                res.append(int(so_far+str(node.val)))
                return 
            # print(node.val)
            if node.left:
                dfs(node.left,so_far+str(node.val))
            if node.right:
                dfs(node.right,so_far+str(node.val))

            # print(left,right)
            
        dfs(root,'')
        # print(res)
        return sum(res)