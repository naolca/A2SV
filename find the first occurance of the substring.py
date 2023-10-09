class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        alpha = 27

        if len(needle) > len(haystack):
            return -1

        def index(s):
            return ord(s) - ord('a') + 1
        
        def hash(s):
            power = len(s) - 1
            hashed = 0
            alpha = 27
            for i, char in enumerate(s):
                hashed += (index(char) * (alpha ** power))
                power -= 1

            return hashed
        def addLast(hash, char):
            return hash * alpha + (index(char))
        def removeFirst(hash, char):
            return hash - (index(char) * (alpha ** (len(needle) - 1)))

        main = hash(needle)
        cand = hash(haystack[:len(needle)])
        if main == cand:
            # print('here')
            return 0
        
        for r in range(len(needle), len(haystack)):
            # print(r, r - len(needle))
            cand = removeFirst(cand, haystack[r - len(needle)])
            cand = addLast(cand, haystack[r])
            if cand == main:
                # print(r)
                return r - len(needle) + 1
        return -1

        



        
