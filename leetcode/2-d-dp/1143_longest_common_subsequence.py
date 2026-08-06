"""
LeetCode 1143. Longest Common Subsequence
Topic: 2-D DP
Difficulty: Medium
Link: https://leetcode.com/problems/longest-common-subsequence/

Approach:
- 2D DP backward tabulation.
- dp[i][j] = length of LCS of text1[i:] and text2[j:].
- Recurrence:
    if text1[i] == text2[j]:
      dp[i][j] = 1 + dp[i+1][j+1]
    else:
      dp[i][j] = max(dp[i+1][j], dp[i][j+1])
- Base: dp[m][*] = dp[*][n] = 0.
- Answer: dp[0][0].

Complexity:
- Time:  O(m * n)
- Space: O(m * n)
"""

from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]


if __name__ == "__main__":
    s = Solution()
    print("abcde", "ace", "->", s.longestCommonSubsequence("abcde", "ace"))
    print("abc", "abc", "->", s.longestCommonSubsequence("abc", "abc"))
    print("abc", "def", "->", s.longestCommonSubsequence("abc", "def"))
