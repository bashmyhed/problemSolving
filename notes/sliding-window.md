# Sliding Window — Notes

## 3. Longest Substring Without Repeating Characters
- **Pattern:** Variable-size sliding window with a hash set.
- **Key idea:** Keep a window `[l, i]` of unique characters. When `s[i]` duplicates
  a character already in the window, shrink from the left until it's unique again.
- **Why it works:** Every character is added/removed at most once, so the window
  always represents the longest valid substring ending at `i`.
- **Edge cases:** Empty string returns 0. All-equal string leaves window size 1.
- **Optimization note:** For ASCII input, a fixed-size array can replace the set
  for slightly faster membership checks.
- **Cost:** O(n) time, O(min(n, charset)) space.
