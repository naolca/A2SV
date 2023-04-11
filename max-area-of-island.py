class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        d=defaultdict()
        general_seen=set()
        maxx=0
        inBound=lambda r,c:0<=r<len(grid) and 0<=c<len(grid[0])
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
    
        def dfs(r,c,seen):
            
            seen.add((r,c))
            general_seen.add((r,c))
            for dx,dy in directions:
                new_r=r+dx
                new_c=dy+c
                if (new_r,new_c) not in seen and inBound(new_r,new_c) and grid[new_r][new_c]==1:
                    dfs(new_r,new_c,seen)
            # print((r,c),seen)
            return len(seen)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1 and (r,c) not in general_seen:
                    seen=set()
                    maxx=max(maxx,dfs(r,c,seen))
                    seen.clear()
        return maxx