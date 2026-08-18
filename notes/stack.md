# Stack — Notes

## 503. Next Greater Element II
- **Pattern:** Monotonic stack (decreasing) over a circular array.
- **Key idea:** Traverse indices `2n-1 → 0`. The stack holds candidates; pop while
  `stack[-1] <= cur` so only strictly greater values remain.
- **Circular trick:** Use `i % n` to read values; virtual doubling lets each element
  see the wrap-around candidates that come "after" it.
- **Why `i < n` guard:** Only the first `n` iterations correspond to real result slots;
  later iterations just rebuild the stack for wrap-around context.
- **Cost:** O(n) time, O(n) space.

## 20. Valid Parentheses
- **Pattern:** Balanced bracket validation with a stack.
- **Key idea:** Push opening brackets; on a closing bracket, check that it matches
  the top of the stack, then pop. If it doesn't match or the stack is empty,
  the string is invalid.
- **Why it works:** Stack tracks the most recent unmatched open bracket, so each
  closing bracket pairs with its nearest unmatched opener.
- **Edge cases:** Unexpected characters return False immediately; empty string is
  valid (`not stack` is True).
- **Cost:** O(n) time, O(n) space.
