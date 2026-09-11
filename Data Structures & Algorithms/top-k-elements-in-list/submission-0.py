class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        result = []
        for i in nums:
            freq[i] += 1
        for i,v in sorted(freq.items(),key=lambda x:x[1],reverse=True):
            if k == 0:
                return result
            result.append(i)
            k -= 1
        return result