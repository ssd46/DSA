class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for i in range(len(nums)):
            remainder=target-nums[i]
            if(remainder in hm):
                return ([hm[remainder],i])
            hm[nums[i]]=i
