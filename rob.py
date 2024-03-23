class Solution:
    
    def robHouse(self,nums):
        if len(nums)==0:
            return
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
    
        return max(nums[0]+self.robHouse(nums[2:]),self.robHouse(nums[1:]))
    
    
    
    
    
    


print(Solution().robHouse([1,2,3,1]))