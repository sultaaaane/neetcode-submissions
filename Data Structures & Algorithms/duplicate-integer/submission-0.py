class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = nums
        i =0
        while i < len(nums):
            j = i + 1
            while j < len(check):
                if (nums[i] == check[j]):
                    return True
                j += 1
            i += 1
        return False  