"""
LeetCode 3731. Find Missing Elements
Topic: Arrays & Hashing
Difficulty: Easy
Link: https://leetcode.com/problems/find-missing-elements/

Approach:
- Optimized: use a hash set.
- Track min and max while building the set of existing numbers.
- Scan the range [min, max) and collect values not present in the set.

Complexity:
- Time:  O(n)
- Space: O(n)
"""

from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        m = nums[0]
        mn = nums[0]
        exists = set()
        result = []
        for i in nums:
            exists.add(i)
            m = max(m, i)
            mn = min(mn, i)
        for i in range(mn, m):
            if i not in exists:
                result.append(i)
        return result


if __name__ == "__main__":
    s = Solution()
    print([4, 3, 2, 7, 8, 2, 3, 1], "->", s.findMissingElements([4, 3, 2, 7, 8, 2, 3, 1]))
    print([1, 1], "->", s.findMissingElements([1, 1]))
    print([1, 2, 3], "->", s.findMissingElements([1, 2, 3]))
