class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max=float('-inf')
        sum=0
        startindex=0
        endindex=0
        for i in nums:
            if(sum==0):
                index=nums.index(i)
            sum+=i
            if(sum>max):
                max=sum
                startindex=index
                endindex=nums.index(i)
            if(sum<0):
                sum=0
        print(startindex,endindex)
        print(nums[startindex:endindex+1])
        return max
        