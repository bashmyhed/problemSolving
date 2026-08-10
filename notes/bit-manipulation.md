# Bit Manipulation — Notes

## 136. Single Number
- **Pattern:** XOR cancellation.
- **Key idea:** `a ^ a = 0` and `a ^ 0 = a`. XOR of all numbers cancels every
  duplicate, leaving only the single non-repeated value.
- **Why it works:** Only one number appears once; the rest appear exactly twice,
  so pairing always cancels regardless of order (XOR is commutative/associative).
- **Edge cases:** Single-element array `[1] -> 1`; any order of elements works.
- **Cost:** O(n) time, O(1) space.
- **Trade-off vs set:** Set needs O(n) extra space; XOR gives constant space.