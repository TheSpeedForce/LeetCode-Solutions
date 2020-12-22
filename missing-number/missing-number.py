class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        mainsum = sum(range(n+1))
        arrsum = sum(nums)
        return mainsum-arrsum
