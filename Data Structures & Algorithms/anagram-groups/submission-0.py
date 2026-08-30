class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       groups={}
       for str in strs:
            label = ''.join(sorted(str))
            if label not in groups:
                groups[label]=[]
            groups[label].append(str)
       return list(groups.values())     