# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        nodes = defaultdict(list)
        def dfs(node):
            if not node:
                return
            nodes[node] = []
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        

        def lister(node):
            if not node:
                return [None]
           
            nodes[node] =  [node.val] + lister(node.left) + lister(node.right)
            return nodes[node]
        
        lister(root)
        seen = set()
        final = []
        for node in nodes:
            cnt = 0
            for other in nodes:
                if node != other and nodes[node] == nodes[other]:
                    # print(node, other)
                    # print(nodes[node])
                    seen.add(other)
                    cnt += 1
            if cnt > 0 and node not in seen:
                seen.add(node)
                final.append(node)
                
                
        return final




        
