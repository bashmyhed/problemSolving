"""
LeetCode 189. Rotate Array
Topic: Arrays & Hashing
Difficulty: Medium
Link: https://leetcode.com/problems/rotate-array/

Approach:
- Brute force: rotate the array k times by one step each iteration.
- Optimized: reverse-based in-place rotation.
  1. Reverse the entire array.
  2. Reverse the first k elements.
  3. Reverse the last n-k elements.

Complexity:
- Brute force: Time O(n * k), Space O(1)
- Optimized:    Time O(n), Space O(1)
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        if k == 0:
            return

        def reverse(lo: int, hi: int) -> None:
            while lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


if __name__ == "__main__":
    def run(nums, k, expected):
        s = Solution()
        s.rotate(nums, k)
        print(nums, "rotate by", k, "->", nums)

    run([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4])
    run([-1, -100, 3, 99], 2, [3, 99, -1, -100])
