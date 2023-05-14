class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        ancestors = defaultdict(list)
        pre = [0 for i in range(n)]
        d = defaultdict(list)

        for f, t in edges:
            d[f].append(t)
            pre[t] += 1
            ancestors[t].append(f)

        todo = deque()
        for i in range(n):
            if pre[i] == 0:
                todo.appendleft(i)
        res = [set() for _ in range(n)]
        while todo:
            curr = todo.pop()
            for decendent in d[curr]:

                res[decendent].add(curr)
                res[decendent].update(res[curr])

                pre[decendent] -= 1
                if pre[decendent] == 0:
                    todo.appendleft(decendent)
        
        res = [(sorted(list(s))) for s in res]
        
        return res
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        res = self.getAncestors(numCourses,prerequisites)
        # print(res)
        ans = []
        for i in range(len(queries)):
            if queries[i][0] in res[queries[i][1]]:
                ans.append(True)
            else:
                ans.append(False)
        return ans

            
            
        return []
