class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = []
        size = len(nums)
        for i in range(size):
            sums.append(sum(nums[:i+1]))
        return sums
