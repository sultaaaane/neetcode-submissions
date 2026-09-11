class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        graph = {}
        for i , v in enumerate(nums):
            graph[v] = i
        for i, v in enumerate(nums):
            diff = target - v
            if diff in graph and i != graph[diff]:
                return[i,graph[diff]]
        return []