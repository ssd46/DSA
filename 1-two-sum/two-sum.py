class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        id={}
        for i in range(len(nums)):
            res=target-nums[i]
            if res in id:
                return [i,id[res]]
            id[nums[i]]=i
            
