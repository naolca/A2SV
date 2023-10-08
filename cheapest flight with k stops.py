class Solution: 
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int: 
        graph = defaultdict(list) 
        for s, d, p in flights: 
            graph[s].append((d, p)) 
     
        def min_price(start): 
            prices = {node: inf for node in graph } 
            prices[start] = 0 
 
            heap = [(0, start, 0)] 
            seen = set() 
 
            while heap: 
               
                curr_price, curr_node, stops = heappop(heap) 
                if curr_node == dst: 
                    return curr_price 
 
                if (curr_node, stops) in seen: 
                    continue 
                seen.add((curr_node, stops)) 
                if stops > k: 
                    continue  
                for nei, price in graph[curr_node]: 
                 
                    heappush(heap, (curr_price + price, nei, stops + 1)) 
            return -1 
         
        return min_price(src)
