class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        od=defaultdict(list)
        for s in strs:
            count=[0]*26
            for e in s:
                count[ord(e)-ord('a')]+=1
            od[tuple(count)].append(s)
        return list(od.values())
        