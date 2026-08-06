# Math & Geometry — Notes

## 3345. Smallest Number
- **Pattern:** Digit-product divisibility scan.
- **Key idea:** If `n % 10 == 0`, product of digits is `0`, divisible by any `t` → return `n`.
  Otherwise scan upward and check whether the product of the two least-significant
  digits is divisible by `t`.
- **Why last two digits:** The problem guarantees a small-step solution; the product
  of the last two digits stabilizes divisibility quickly.
- **Edge cases:** Single-digit `n` → `dig1 == 0` so product is just `dig2`.
- **Cost:** O(k) time where `k` is steps until match (small in practice), O(1) space.
- **Caution:** The two-digit product heuristic is specific to this problem's constraints;
  do not generalize to "digit product of the whole number" without verification.
