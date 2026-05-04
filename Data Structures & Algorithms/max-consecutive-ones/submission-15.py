class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxValue = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
                maxValue = max(count, maxValue)
            else:
                count = 0
        return maxValue

        