class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for i in strs:
            strssorted = "".join(sorted(i))
            result[strssorted].append(i)
        return list(result.values())