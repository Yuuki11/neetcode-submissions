class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxValue = 0
        for num in nums:
            if num == 1:
                count += 1
                maxValue = max(count, maxValue)
            else:
                count = 0
        return maxValue

        