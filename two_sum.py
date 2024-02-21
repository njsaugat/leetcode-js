class Solution:
    
    def two_sum(self,nums,target):
        
        hashset={}

        for i,num in enumerate(nums):
            diff=target-num
            if diff in hashset:
                return [hashset[diff],i]
            
            hashset[num]=i            
            
        
        return [-1,-1]