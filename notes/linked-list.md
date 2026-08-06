# Linked List — Notes

## 2. Add Two Numbers
- **Pattern:** Dummy head + carry propagation.
- **Key idea:** Build result with a `dummy` node and `tail` pointer. At each step use
  `0` when a list is exhausted (`val if node else 0`). Continue while `l1 or l2 or carry`.
- **Why dummy head:** Avoids special-casing the first node and gives a clean `dummy.next`.
- **Edge cases:** Unequal lengths, trailing carry (e.g. 999 + 999 → 1998).
- **Simpler loop:** `while l1 or l2 or carry != 0` removes the need for a separate
  post-loop carry append.
- **Cost:** O(max(m, n)) time, O(max(m, n)) space for output.
