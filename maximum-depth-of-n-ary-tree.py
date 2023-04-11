"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        max_depth=[0]
        def dfs(node,depth):
            # nonlocal max_depth
            # print(depth,max_depth)
            print('not getting here')
            max_depth[0]=max(max_depth[0],depth)
            for child in node.children:
                # print(child.val,depth)
                dfs(child,depth+1)
        dfs(root,0)
        return max_depth[0]+1