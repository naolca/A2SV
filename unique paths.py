class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1

        for i in range(1, n):
            dp[0][i] += 1

        for i in range(1, m):
            dp[i][0] += 1

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r][c - 1] + dp[r - 1][c]
        return dp[m - 1][n - 1]
        
