# 1-D DP — Notes

## 322. Coin Change
- **Pattern:** Unbounded knapsack / min-coin DP.
- **State:** `dp[i]` = minimum coins to make amount `i`.
- **Base:** `dp[0] = 0`; everything else `inf`.
- **Transition:** `dp[i] = min(dp[i], dp[i - coin] + 1)` for each coin `≤ i`.
- **Answer:** `dp[amount]` if finite, else `-1`.
- **Why it works:** Every amount is built from smaller already-solved amounts.
- **Cost:** O(amount × coins) time, O(amount) space.
- **Watch out:** Initialize with `inf`, not `0`, so `min` works correctly.
