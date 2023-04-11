class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        d=defaultdict(list)
        for i in range(len(graph)):
            for number in graph[i]:
                d[i].append(number)
        # print(d)
        # return [[]]
        res=[]
        def dfs(i,curr=[]):
            # print(curr)
            if i>=len(graph):
                if curr and curr[-1]==len(graph)-1:
                    res.append(curr)
                return
            if curr and curr[-1]==len(graph)-1:
                    res.append(curr)

            for neighboor in d[i]:
                china=curr.copy()
                china.append(neighboor)
                dfs(neighboor,china)
        dfs(0,[0])
        return res