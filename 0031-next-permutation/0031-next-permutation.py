class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        idx=n-2
        while(idx>=0 and nums[idx]>=nums[idx+1]):
            idx-=1
        if(idx==-1):
            return nums.reverse()
        nxtidx=n-1
        while(nums[nxtidx]<=nums[idx]):
            nxtidx-=1
        nums[idx],nums[nxtidx]=nums[nxtidx],nums[idx]
        start=idx+1
        end=n-1
        while(start<end):
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
        return nums
        


        #         n=len(nums)
        # bp=-1
        # while(n>=0):
        #     if(nums[n-2]>=nums[n-1]):
        #         n-=1
        #     else:
        #         bp=n-2
        #         break

     
        # if(bp==-1):
        #     return nums.reverse()
        
        # for i in range(len(nums)-1,-1,-1):
        #     if(nums[i]>nums[bp]):
        #         nums[i],nums[bp]=nums[bp],nums[i]
        #         print(nums)
        #         break
        # si=bp+1
        # ei=len(nums)-1
        # while(si<ei):
        #     nums[si],nums[ei]=nums[ei],nums[si]
        #     si+=1
        #     ei-=1

        # return nums