class Solution:
    def countOrders(self, n: int) -> int:

        MOD = 10 ** 9 + 7

        def fact(n):
            if n == 1:
                return 1
            factorial = ((n % MOD) * fact(n - 1)) % MOD
            return factorial
        # print(fact(4))
        def pow(base, exponent):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                half_result = (pow(base, exponent // 2)) % MOD
                return half_result * half_result
            else:
                half_result =( pow(base, (exponent - 1) // 2)) % MOD
                return half_result * half_result * base
        print(pow(2, 5))

        event = fact(2 * n) % MOD
        sample_space = pow(2, n) 
        ans = ((event) * (pow(sample_space, MOD - 2)))% MOD
        return ans

        

        

        
        
