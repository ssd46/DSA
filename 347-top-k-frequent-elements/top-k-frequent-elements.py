class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqd={}
        for i in nums:
            if i in freqd:
                freqd[i]+=1
            else:
                freqd[i]=1
        fre=[[] for i in range(len(nums)+1)]
        for n,f in freqd.items():
            fre[f].append(n)
        res=[]
        for i in range(len(fre)-1,0,-1):
            for j in fre[i]:
                res.append(j)
            if(len(res)==k):
                return res
        
        