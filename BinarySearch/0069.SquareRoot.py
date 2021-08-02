class Solution:
    def mySqrt(self, x: int) -> int:
        low, high, root = 1, x // 2, 0
        while low < high:
            mid = (low + high) // 2
            if mid * mid < x:
                root = mid
                low = mid + 1
            else:
                high = mid - 1
        return root



s = Solution()
x = 182
print(s.mySqrt(x))