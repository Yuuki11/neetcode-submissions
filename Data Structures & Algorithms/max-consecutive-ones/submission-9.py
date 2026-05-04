class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maxValue = 0
        for num in nums:
            if num == 1:
                counter += 1
                maxValue = max(counter, maxValue)
            else:
                counter = 0
        return maxValue