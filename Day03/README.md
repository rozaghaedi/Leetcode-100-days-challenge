# LC14 — Longest Common Prefix (Python)

**Problem:** Given `strs: List[str]`, return the longest common prefix. If none, return `""`.

**Approach:** Vertical scan. Use the first string as a baseline; for each index `i`, check the same index in all other strings. Stop at the first mismatch and return `strs[0][:i]`.


