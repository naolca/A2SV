class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = []
        for char in s:
            if not stack:
                stack.append([char, 1])
                continue
            if char == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
            
            if stack[-1][1] == k:
                stack.pop()
        ans = []
        for char, v in stack:
            ans.append(char * v)
        return "".join(ans)
        
        
