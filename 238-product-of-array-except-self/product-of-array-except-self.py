class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[1]*len(nums)
        suff=[1]*len(nums)
        out=[]
        pre[0]=1
        suff[len(nums)-1]=1
        for i in range(1,len(nums)):
            pre[i]=pre[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            suff[i]=suff[i+1]*nums[i+1]
        for i in range(len(nums)):
            out.append(pre[i]*suff[i])
        return out







        