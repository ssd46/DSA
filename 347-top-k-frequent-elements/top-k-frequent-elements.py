class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        res=[[] for i in range(len(nums)+1)]
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for g,v in freq.items():
            res[v].append(g)
        out=[]
        for i in range(len(res)-1,0,-1):
            for j in res[i]:
                out.append(j)
                if(len(out)==k):
                    return out
          

  
        