class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        mw=0
        freq={}
        for r in range(len(s)):
            freq[s[r]]=1+freq.get(s[r],0)
            if(((r-l+1)-max(freq.values()))>k):
                freq[s[l]]-=1
                l+=1
            mw=max(mw,r-l+1)
        return mw


        