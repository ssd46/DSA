class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        marea=0
        right=len(height)-1
        while(left<right):
            area=(right-left)*min(height[left],height[right])
            if area>marea:
                marea=area
            if(height[left]<height[right]):
                left+=1
            elif(height[left]>height[right]):
                right-=1
            else:
                left+=1

        return marea
            

        