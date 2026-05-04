class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        lastElement = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = lastElement
            lastElement = max(temp, lastElement)
        return arr