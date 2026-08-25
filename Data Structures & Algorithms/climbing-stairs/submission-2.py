class Solution:
    def fib_seq(self, n: int) -> int:
        if n <= 1:
            return n
        prev, curr = 0, 1
        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr
        return curr

    def climbStairs(self, n: int) -> int:
        return self.fib_seq(n + 1)
