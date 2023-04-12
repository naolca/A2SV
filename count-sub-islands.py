class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        giant_set=set()
        for r in range(len(grid1)):
            for c in range(len(grid1[0])):
                if grid1[r][c]==1:
                    giant_set.add((r,c))
        inBound=lambda r,c:0<=r<len(grid2) and 0<=c<len(grid2[0])
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
    
        def dfs(r,c,seen):
            
            seen.add((r,c))
            general_seen.add((r,c))
            for dx,dy in directions:
                new_r=r+dx
                new_c=dy+c
                if (new_r,new_c) not in seen and inBound(new_r,new_c) and grid2[new_r][new_c]==1:
                    dfs(new_r,new_c,seen)
            # print((r,c),seen)
            return seen
        general_seen=set()
        stubs=0
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                if grid2[r][c]==1 and (r,c) not in general_seen:
                    seen=set()
                    island=dfs(r,c,seen)
                    if island&giant_set==island:
                        stubs+=1
                    seen.clear()
        return stubs