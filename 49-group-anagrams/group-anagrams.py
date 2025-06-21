class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sd=defaultdict(list)
        for s in strs:
            sd[''.join(sorted(s))].append(s)
        return list(sd.values())
 
     
        