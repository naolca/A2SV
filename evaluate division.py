class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        def dijkstra(graph, start, end):
           
            
            heap = []
            seen = set()
            heappush(heap, (1, start))

            while heap:
                
                # print(heap)
                curr_weight, curr_node = heappop(heap)
                if curr_node == end:
                    return curr_weight
                
                if curr_node in seen:
                    continue
                seen.add(curr_node)
                for nei, weight in graph[curr_node]:
                    new_weight = curr_weight * weight
                    # print(node, new_weight, nei)
                    heappush(heap, (new_weight, nei))
            return -1.0
        graph = defaultdict(list)
        variables = set()
        for i in range(len(equations)):
            s, e = equations[i]
            variables.add(s)
            variables.add(e)
            weight = values[i]
            graph[s].append((e, weight))
            graph[e].append((s, 1 / weight))
        # print(graph)


        
        ans = []
        for start, end in queries:
            if start not in variables or end not in variables:
                ans.append(-1)
                continue
            ans.append(dijkstra(graph, start, end))
        return ans
            
