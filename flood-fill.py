class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        needed_color=image[sr][sc]
        def dfs(r,c,seen):
            if (r,c) in seen or r>=len(image) or c>=len(image[0]) or c<0 or r<0 or image[r][c]!=needed_color:
                return
            seen.add((r,c))
            image[r][c]=color
            dfs(r,c+1,seen)
            dfs(r,c-1,seen)
            dfs(r+1,c,seen)
            dfs(r-1,c,seen)
        seen=set()
        dfs(sr,sc,seen)
        return image