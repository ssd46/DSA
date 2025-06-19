class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            charcount=[0]*26
            for c in s:
                charcount[ord(c)-ord('a')]+=1
            res[tuple(charcount)].append(s)
        return list(res.values())
     
        