"""
LeetCode 322. Coin Change
Topic: 1-D DP
Difficulty: Medium
Link: https://leetcode.com/problems/coin-change/

Approach:
- Bottom-up DP.
- dp[i] = minimum number of coins to make amount i.
- Base: dp[0] = 0.
- Transition:
    for each coin <= i:
      dp[i] = min(dp[i], dp[i - coin] + 1)
- If dp[amount] stays infinite, there is no valid combination.

Complexity:
- Time:  O(n * m), where n = amount, m = len(coins)
- Space: O(n)
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin > i:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == float("inf"):
            return -1
        return dp[amount]


if __name__ == "__main__":
    s = Solution()
    print([1, 2, 5], 11, "->", s.coinChange([1, 2, 5], 11))
    print([2], 3, "->", s.coinChange([2], 3))
    print([1], 0, "->", s.coinChange([1], 0))
