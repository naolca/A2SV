class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        dp = [[-1] * 26 for _ in range(len(s))]
        dp[-1][ord(s[-1]) - ord('a')] = len(s) - 1

        

        for i in range(len(s) - 2, -1, -1):
            dp[i] = dp[i + 1].copy()
            dp[i][ord(s[i]) - ord('a')] = i
        # print(dp)
        ans = 0
        for word in words:
            i = 0
            valid = True
            for char in word:
                if i >= len(s):
                    valid = False
                    break
                if dp[i][ord(char) - ord('a')] == -1:
                    # print(word)
                    valid = False
                    break
                i = dp[i][ord(char) - ord('a')] + 1
                # print(char, i)
            if valid:
                ans += 1

        return ans





        
                






        


        
