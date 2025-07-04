class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hass=set()
        l=0
        le=0
        for r in range(len(s)):
            while(s[r] in hass):
                hass.remove(s[l])
                l+=1


            hass.add(s[r])
            le=max(le,r-l+1)

        return le
       
            
            
        