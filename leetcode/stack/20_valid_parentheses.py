"""
LeetCode 20. Valid Parentheses
Topic: Stack
Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses/

Approach:
- Use a stack for open brackets.
- On seeing an open bracket, push it.
- On seeing a close bracket:
    - if stack is empty, invalid
    - if top matches, pop it
    - otherwise invalid
- Ignore unexpected characters by returning False immediately.
- At end, stack must be empty for the string to be valid.

Complexity:
- Time:  O(n)
- Space: O(n)
"""

from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c not in "({[]})":
                return False
            if c in "([{":
                stack.append(c)
            elif not stack:
                return False
            elif (
                (c == ")" and stack[-1] == "(")
                or (c == "]" and stack[-1] == "[")
                or (c == "}" and stack[-1] == "{")
            ):
                stack.pop()
            else:
                return False
        return not stack


if __name__ == "__main__":
    s = Solution()
    for test in ["()", "()[]{}", "(]", "([)]", "{[]}", ""]:
        print(test, "->", s.isValid(test))
