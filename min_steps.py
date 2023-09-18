class Solution:
    def minSteps(self, n: int) -> int:
        memo = {}

        def dp(copied, screen):
            if (copied, screen) in memo:
                return memo[(copied, screen)]
            if screen == n:
                return 0
            if screen > n:
                return inf
            # print(copied, screen)
            
            
            # print(copied, screen)
            copy = float('inf')
            if copied != screen:
                copy = 1 + dp(screen, screen)
            paste = inf
            if copied > 0:
                paste = 1 + dp(copied, screen + copied)
            memo[(copied, screen)] =  min(copy, paste)
            return memo[(copied, screen)]


        return dp(0, 1)
        
