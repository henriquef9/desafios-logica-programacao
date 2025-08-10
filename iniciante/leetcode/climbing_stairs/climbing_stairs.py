
def climbStairs(n):

    memo = [-1] * n

    def climb(n):

        if memo[n - 1] != -1:
            return memo[n - 1]

        if n < 0:
            return 0
        
        if n <= 3:
            memo[n - 1] = n
            return n
        
        memo[n - 1] = climb(n - 1) + climb(n - 2)

        return memo[n - 1]
        
    return climb(n)
        


print(climbStairs(1))
print(climbStairs(2))
print(climbStairs(3))
print(climbStairs(4))
print(climbStairs(5))
print(climbStairs(6))
print(climbStairs(7))
print(climbStairs(8))
        