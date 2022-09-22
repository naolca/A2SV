class Solution:
    def isValid(self, s: str) -> bool:
            brackets = {"]":"[", "}":"{", ")":"("}
            stack=[]
            for c in s:
                if c not in brackets:#this checks if the symbol is an opening.
                    stack.append(c)
                    continue
                if not stack or brackets[c] != stack[-1]:#this means that if the current symbol is a closing and if the stack is empty or the last added item is not the opener for the current closer.
                    return False
                stack.pop()

            return not stack
