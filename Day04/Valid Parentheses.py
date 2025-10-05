class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        expect={'(':')' , '{':'}' , '[':']'}

        for ch in s:
            if ch in expect:
                stack.append(expect[ch])
            else :
                if not stack or stack.pop() != ch:
                    return False
        return not stack  
        

