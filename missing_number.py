class Solution:
    
    def missing_num(self,nums):
        
        max=len(nums)
        sum=(max*(max+1))//2
        
        missing=sum
        for num in nums:
            missing-=num
        
        return missing 
        