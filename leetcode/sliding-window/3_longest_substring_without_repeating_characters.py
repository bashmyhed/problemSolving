"""
LeetCode 3. Longest Substring Without Repeating Characters
Topic: Sliding Window
Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Approach:
- Sliding window with a character set.
- Expand the right pointer `i` over the string.
- When `s[i]` is already in the set, shrink the window from the left by
  removing characters until the duplicate is gone.
- Track the longest valid window seen.

Complexity:
- Time:  O(n)
- Space: O(min(n, charset))
"""

from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxL = 0
        seen = set()

        for i, c in enumerate(s):
            while c in seen:
                seen.remove(s[l])
                l += 1
            seen.add(c)
            maxL = max(maxL, i - l + 1)

        return maxL


if __name__ == "__main__":
    s = Solution()
    print("abcabcbb", "->", s.lengthOfLongestSubstring("abcabcbb"))
    print("bbbbb", "->", s.lengthOfLongestSubstring("bbbbb"))
    print("pwwkew", "->", s.lengthOfLongestSubstring("pwwkew"))
    print("", "->", s.lengthOfLongestSubstring(""))