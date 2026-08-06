"""
LeetCode 503. Next Greater Element II
Topic: Stack / Monotonic Stack
Difficulty: Medium
Link: https://leetcode.com/problems/next-greater-element-ii/

Approach:
- Use a monotonic decreasing stack over a virtual doubled traversal.
- Traverse indices from 2*n-1 down to 0.
- Pop while stack[-1] <= current value to keep only stronger candidates.
- Only assign result when i < n, i.e. during the first/real pass.
- Push current value; duplicates are fine because we compare by value.

Complexity:
- Time:  O(n)
- Space: O(n)
"""

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack: List[int] = []
        n = len(nums)
        res = [-1] * n

        for i in range((2 * n) - 1, -1, -1):
            cur = nums[i % n]

            while stack and stack[-1] <= cur:
                stack.pop()

            if stack and (i < n):
                res[i] = stack[-1]

            stack.append(cur)

        return res


if __name__ == "__main__":
    samples = [
        [1, 2, 1],
        [1, 2, 3, 4, 3],
    ]
    s = Solution()
    for nums in samples:
        print(nums, "->", s.nextGreaterElements(nums))
