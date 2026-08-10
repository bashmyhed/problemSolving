"""
LeetCode 136. Single Number
Topic: Bit Manipulation
Difficulty: Easy
Link: https://leetcode.com/problems/single-number/

Approach:
- XOR every number together.
- Since a ^ a = 0 and a ^ 0 = a, all pairs cancel out and only the
  single non-duplicate remains.

Complexity:
- Time:  O(n)
- Space: O(1)
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == "__main__":
    s = Solution()
    print([2, 2, 1], "->", s.singleNumber([2, 2, 1]))
    print([4, 1, 2, 1, 2], "->", s.singleNumber([4, 1, 2, 1, 2]))
    print([1], "->", s.singleNumber([1]))