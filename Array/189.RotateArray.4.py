from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]

s = Solution()
L, k = [1, 2, 3, 4, 5, 6, 7], 3
# L, k = [-1, -100, 3, 99], 2
s.rotate(L, k)
print(L)
