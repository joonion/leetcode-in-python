from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n, k = len(nums), k % len(nums)
        start = count = 0
        while count < n:
            curr, prev = start, nums[start]
            while True:
                next = (curr + k) % n
                nums[next], prev = prev, nums[next]
                curr = next
                count += 1
                if start == curr:
                    break
            start += 1

s = Solution()
# L, k = [1, 2, 3, 4, 5, 6, 7], 3
L, k = [-1, -100, 3, 99], 2
s.rotate(L, k)
print(L)