"""
LeetCode 3345. Smallest Number
Topic: Math / Number Theory
Difficulty: Medium
Link: https://leetcode.com/problems/smallest-number/

Approach:
- If n already ends with 0, its digit product is 0, which is divisible by t.
- Otherwise, scan upward a few values only:
    - Compute the product of the two least-significant digits.
    - If that product is divisible by t, return n.
- Relies on the property that within a small window the last two digits
  produce a product divisible by t.

Complexity:
- Time:  O(k), where k is the number of steps until a match (small in practice)
- Space: O(1)
"""

from typing import List


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        if n % 10 == 0:
            return n

        while True:
            dig2 = n % 10
            dig1 = n // 10
            prod = dig2 if dig1 == 0 else dig1 * dig2
            if prod % t == 0:
                return n
            n += 1


if __name__ == "__main__":
    s = Solution()
    print("n=10, t=2 ->", s.smallestNumber(10, 2))
    print("n=15, t=3 ->", s.smallestNumber(15, 3))
    print("n=38, t=9 ->", s.smallestNumber(38, 9))
