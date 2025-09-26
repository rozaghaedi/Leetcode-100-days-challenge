# LeetCode Problem: https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)          # Convert number to string
        return s == s[::-1]  # Compare with its reversed string
