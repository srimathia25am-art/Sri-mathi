class Solution:
    def reverse(self, x): 
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        rev_str = str(x)[::-1]
        rev = sign * int(rev_str)
        
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        return rev