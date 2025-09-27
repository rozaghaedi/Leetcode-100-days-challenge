# LC13 — Roman to Integer


**Problem:** Convert a valid Roman numeral (1–3999) to an integer.

**Approach:** Scan left → right. If the current symbol’s value is **less than** the next symbol, **subtract** it; otherwise **add** it. This handles subtractive pairs: `IV, IX, XL, XC, CD, CM`.

**Complexity:** `O(n)` time, `O(1)` space.

**Examples**
- `"III"` → `3`
- `"LVIII"` → `58`
- `"MCMXCIV"` → `1994`

**Quick test**
```python
from solution import Solution
s = Solution()
assert s.romanToInt("III") == 3
assert s.romanToInt("LVIII") == 58
assert s.romanToInt("MCMXCIV") == 1994
