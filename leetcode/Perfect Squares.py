class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n for _ in range(n+1)]

        dp[0] = 0

        for target in range(1, n+1):
            for s in range(1,target+1):
                sq = s*s
                if target - sq < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target-sq])
        return dp[n]

