class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for index, i in enumerate(s):
            
            if i != ']':
                stack.append(i)
            else:
                temp_string = ''
                while stack[-1] != '[':
                    k = stack.pop(-1)
                    temp_string= k + temp_string
                stack.pop(-1)
                i = ''
                while len(stack) > 0 and stack[-1].isnumeric():
                    i=(stack[-1])+i
                    stack.pop(-1)
                temp_string = int(i)*temp_string
                stack.append(temp_string)
        string_2b_returned=''
        for strings in stack:
            string_2b_returned+=strings
        return string_2b_returned