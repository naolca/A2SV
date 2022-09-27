class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        list_2b_returned = [0] * len(temperatures)
        stack = []
        
        for index, temperature in enumerate(temperatures):
            if not stack:
                stack.append((index,temperature))
            else:
                while stack and temperature > stack[-1][1]:
                    top = stack.pop()
                    list_2b_returned[top[0]] = index - top[0]
                stack.append((index, temperature))
        
        return list_2b_returned
        