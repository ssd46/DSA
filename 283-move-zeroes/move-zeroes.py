class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos=0
        if(len(nums)==1):
            return nums
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[pos],nums[i]=nums[i],nums[pos]
                pos+=1
               
        return nums
       
        