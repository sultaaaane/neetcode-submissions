class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        current = 0
        i = 0
        length = len(nums)
        while i < length:
            if nums[i] == 0:
                current = 0
                maximum = max(maximum,current)
            else:
                current += 1
            maximum = max(maximum,current)
            i += 1
        return maximum