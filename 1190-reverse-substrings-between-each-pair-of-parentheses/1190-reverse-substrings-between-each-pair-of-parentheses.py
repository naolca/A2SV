class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]#the stack i am going to use
        temp=[]#this will hold the inner most to be reversed string.
        answer=""
        temp=[]
        length=len(s)
        for i in range(length):
            if s[i]==")":#this will be true on the first ) sign and this happens right after the inner string
                while stack:
                    character=stack.pop()
                    if character=="(":
                        break
                    temp.append(character)
                stack.extend(temp)
                temp=[]
            else:
                stack.append(s[i])
            
        for character in stack:
            answer+=character
        return answer

                