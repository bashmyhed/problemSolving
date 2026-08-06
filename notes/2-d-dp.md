# 2-D DP — Notes

## 1143. Longest Common Subsequence
- **Pattern:** 2D DP on two strings (subsequence, not substring).
- **State:** `dp[i][j]` = LCS length of `text1[i:]` and `text2[j:]`.
- **Recurrence (backward):**
  - match: `dp[i][j] = 1 + dp[i+1][j+1]`
  - mismatch: `dp[i][j] = max(dp[i+1][j], dp[i][j+1])`
- **Base:** Last row/col are `0` (Python auto via `(m+1) x (n+1)` grid).
- **Answer:** `dp[0][0]`.
- **Subsequence vs substring:** We can skip characters (no contiguous requirement),
  hence taking `max` of both skip directions.
- **Cost:** O(m × n) time and space.
