class Solution:
    def reverse(self, x: int) -> int:
        rev = int(str(abs(x))[::-1])
        ret = rev if -(2**31)-1 < rev < 2**31 else 0
        return ret if x >= 0 else -1 * ret

s = Solution()
print(s.reverse(-123))