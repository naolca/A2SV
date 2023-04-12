class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        N = len(bombs)
        adjList = defaultdict(set)
   

        for i in range(N):
            for j in range(i+1, N):
                distance = sqrt((bombs[i][0]-bombs[j][0])**2 + (bombs[i][1]-bombs[j][1])**2)
  
                if bombs[i][2] >= distance:
                    adjList[i].add(j)
                if bombs[j][2] >= distance:
                    adjList[j].add(i)

        def dfs(node, visited):

            if node in visited:
                return 0

            visited.add(node)
            detonate = 1
            for neighbour in adjList[node]:
                if neighbour not in visited:
                    detonate += dfs(neighbour, visited)
            
            return detonate
            
        ans = 0
        for i in range(N):
            ans = max(ans, dfs(i, set()))

        return ans