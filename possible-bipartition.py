class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def buildGraph(edges):
            d=defaultdict(list)
            for f,t in edges:
                d[f].append(t)
                d[t].append(f)
            return d
        d=buildGraph(dislikes)
        #the two colors are 1 and -1
        colors=defaultdict(int)
        def dfs(i,curr_color):
            if colors[i]!=0:
                if colors[i]==curr_color:
                    return True
                return False
            colors[i]=curr_color
            for hated in d[i]:
                if not dfs(hated,-curr_color):
                    return False
            return True

        for key in d:
            if colors[key]==0:
                if not dfs(key,1):
                    return False
        return True