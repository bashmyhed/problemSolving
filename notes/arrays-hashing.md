# Arrays & Hashing — Notes

## 189. Rotate Array
- **Pattern:** In-place rotation via reversal.
- **Key idea:** Rotating right by `k` is equivalent to:
  1. reverse whole array
  2. reverse first `k` elements
  3. reverse last `n-k` elements
- **Why it works:** Reversal splits and reorders the two logical halves.
- **Edge cases:** `k` can be larger than `n` → always do `k %= n` first. `k == 0` → return early.
- **Cost:** O(n) time, O(1) space.
- **Brute force reference:** Rotate one step `k` times (O(n*k)); shown in same file.

## 3731. Find Missing Elements
- **Pattern:** Set membership over a bounded range.
- **Key idea:** Put all numbers in a set, then scan `[min, max)` and collect absent values.
- **Why better than sort:** Set lookup is O(1); no O(n log n) sort needed.
- **Edge cases:** Range is `[min, max)` — max itself is not missing by definition here.
- **Cost:** O(n) time, O(n) space.
- **Brute force reference:** Sort + two-pointer walk (O(n log n)); shown in same file.
