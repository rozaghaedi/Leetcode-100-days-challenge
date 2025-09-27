class Solution:
    def romanToInt(self, s: str) -> int:
        val = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
   
        for i in range(len(s) - 1):
            if val[s[i]] < val[s[i + 1]]:
                total -= val[s[i]]
            else:
                total += val[s[i]]
        return total + val[s[-1]]

