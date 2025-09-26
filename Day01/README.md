# 📅 Day 01 – LeetCode 100 Days Challenge

## Problems Solved
1. [Two Sum](https://leetcode.com/problems/two-sum/)  
2. [Palindrome Number](https://leetcode.com/problems/palindrome-number/)

---

## 📝 Notes

### 1. Two Sum
- **Approach**: Use a HashMap (dictionary) to store numbers and their indices while iterating.  
- **Complexity**:  
  - Time: O(n)  
  - Space: O(n)  
- **Key Idea**: For each number, check if `target - num` already exists in the map.

---

### 2. Palindrome Number
- **Approach**: Convert the number to a string and check if it reads the same forwards and backwards.  
- **Complexity**:  
  - Time: O(n) where n is the number of digits  
  - Space: O(1) (ignoring string conversion)  
- **Key Idea**: Simple string reversal is enough, but there’s also a math-based approach without string conversion.
