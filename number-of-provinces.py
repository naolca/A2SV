class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def buildGraph(matrix):
            d=defaultdict(list)
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j]==1:
                        d[i].append(j)
                        d[j].append(i)
            return d
        def dfs(node):
            nonlocal seen
            if node in seen:
                return
            seen.add(node)
            for neighboor in d[node]:
                dfs(neighboor)
            
        d=buildGraph(isConnected)
        seen=set()
        ans=0
        for key in d:
            if key not in seen:
                dfs(key)
                ans+=1
        return ans