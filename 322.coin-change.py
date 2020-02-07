#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()
        def dp(n):
            # # base case
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n < 0:
                return -1
            # 求最小值，所以初始化为正无穷
            res = float("INF")
            for coin in coins:
                subproblem = dp(n - coin)
                # 子问题无解，跳过
                if subproblem == -1:
                    continue
                res = min(res, 1 + subproblem)

            memo[n] =  res if res != float("INF") else -1
            return memo[n]

        return dp(amount)


# @lc code=end

