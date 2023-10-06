# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, target):
        self.result = 0
        cache = {0:1}
        
        self.dfs(root, target, 0, cache)
        
        return self.result
    
    def dfs(self, root, target, currPathSum, cache):
        if root is None:
            return  
        currPathSum += root.val
        oldPathSum = currPathSum - target
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        cache[currPathSum] -= 1
