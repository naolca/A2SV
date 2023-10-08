class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        def dijkstra(graph, start, end):
            distance = defaultdict(float)
            for node in range(n):
                distance[node] = 0
            distance[start] = 1
            heap = []
            
            
            heappush(heap, (-1 , start))
            while heap:
                # print(heap)

                current_prob, node = heappop(heap)
                if node == end:
                    return - current_prob
                
                for nei, prob in graph[node]:
                    new_prob = - current_prob * prob
                    # print(node, nei, new_prob)
                    if new_prob > distance[nei]:
                        # print(nei)
                        distance[nei] = new_prob
                        heappush(heap, ( - distance[nei], nei))
            # print(distance)
            return 0
        
        graph = defaultdict(list)
        for i, edge in enumerate(edges):
            s, d = edge
            graph[s].append((d, succProb[i]))
            graph[d].append((s, succProb[i]))
        # print(graph)
        return dijkstra(graph, start_node, end_node)
        

                
