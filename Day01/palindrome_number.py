# LeetCode Problem: https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindrome
        if x < 0:
            return False
        # Convert to string and check equality with reverse
        return str(x) == str(x)[::-1]
