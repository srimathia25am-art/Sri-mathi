class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # 1. Ignore leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # 3. Convert digits
        num = 0

        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num = num * sign

        # 4. Keep within 32-bit signed integer range
        if num < -2**31:
            return -2**31

        if num > 2**31 - 1:
            return 2**31 - 1

        return num
        