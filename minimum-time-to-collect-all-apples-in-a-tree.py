class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        d=defaultdict(list)
        for f,t in edges:
            d[f].append(t)
            d[t].append(f)
        # print(d)
        seen=set()
        def recur(n):
            if not d[n]:
                if hasApple[n]:
                    return 2
                return 0
            summ=0
            seen.add(n)
            for child in d[n]:
                if child not in seen:
                    summ+=recur(child)
            if not summ:
                if hasApple[n]:
                    return 2
                else:
                    return 0
            return summ+2



        
        
        return max(0,recur(0)-2)