class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Trim leading whitespace
        s = s.lstrip()
        if not s:
            return 0

        # Step 2: Check the sign
        sign = 1
        i = 0
        if s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            i += 1

        # Step 3: Convert digits
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        # Step 4: Apply sign
        num *= sign

        # Step 5: Clamp to 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num
