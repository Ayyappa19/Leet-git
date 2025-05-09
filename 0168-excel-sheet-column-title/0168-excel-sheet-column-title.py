class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ""
        while n > 0:
            n -= 1
            ans = chr(n % 26 + 65) + ans
            n //= 26
        return ans