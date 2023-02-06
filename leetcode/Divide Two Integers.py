class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0) else 1
        quotient = 0
        absDividend = abs(dividend)
        absDivisor = abs(divisor)

        MAX = 2147483647
        MIN = -2147483648

        if divisor == 0 or (dividend == MIN and divisor == -1):
            return MAX

        while absDividend >= absDivisor:
            shift = 0
            while absDividend >= absDivisor << (shift):
                shift += 1
            quotient += 1 << (shift-1)

            absDividend = absDividend - (absDivisor << (shift-1))

        # res = min(max(-2**31, sign * quotient), 2**31)
        return sign * quotient
