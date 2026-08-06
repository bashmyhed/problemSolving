"""
LeetCode 2. Add Two Numbers
Topic: Linked List
Difficulty: Medium
Link: https://leetcode.com/problems/add-two-numbers/

Approach:
- Iterate through both lists with carry.
- Use dummy head for simpler list construction.
- Use 0 when a list is exhausted, instead of separate branches.
- Continue while either list has nodes or carry is non-zero.

Complexity:
- Time:  O(max(m, n))
- Space: O(max(m, n)) for output list
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        tail = dummy

        while l1 is not None or l2 is not None or carry != 0:
            dig1 = l1.val if l1 else 0
            dig2 = l2.val if l2 else 0

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            newnode = ListNode((dig1 + dig2 + carry) % 10)
            carry = (dig1 + dig2 + carry) // 10
            tail.next = newnode
            tail = tail.next

        return dummy.next


def build(values):
    dummy = ListNode(0)
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    s = Solution()
    cases = [
        ([2, 4, 3], [5, 6, 4]),
        ([0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]),
    ]
    for a, b in cases:
        res = s.addTwoNumbers(build(a), build(b))
        print(a, "+", b, "=", to_list(res))
