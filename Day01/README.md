# 📅 Day 01 – LeetCode 100 Days Challenge

## Problems Solved
1. [Two Sum](https://leetcode.com/problems/two-sum/)  
2. [Palindrome Number](https://leetcode.com/problems/palindrome-number/)

---


### 1. Two Sum


This code solves the **Two Sum** problem.  
Given a list of integers (`nums`) and a target number (`target`), the goal is to find **two numbers** in the list whose sum equals the target and return their **indices**.

#### Example

```python
nums = [2, 7, 11, 15]
target = 9
# Output: [0, 1]

---

### 2. Palindrome Number
- **Approach**: Convert the number to a string and check if it reads the same forwards and backwards.  
- **Complexity**:  
  - Time: O(n) where n is the number of digits  
  - Space: O(1) (ignoring string conversion)  
- **Key Idea**: Simple string reversal is enough, but there’s also a math-based approach without string conversion.
