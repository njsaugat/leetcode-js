class Solution:
    
    def rob(self,nums):
        
        def helper(nums):
            if len(nums)==1:
                return nums[0]
            
            if len(nums)==2:
                return max(nums[0],nums[1])
            return max(nums[0]+helper(nums[2:]),helper(nums[1:]))
            
        
        return helper(nums)
    
    
print(Solution().rob([1,2,3,1]))