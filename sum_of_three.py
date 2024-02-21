class Solution:
    def three_sum(self,nums):
        nums.sort()
        res=[]
        for i,num in enumerate(nums):
            
            if i>0 and nums[i-1]==num:
                continue
            
            left,right=i+1,len(nums)-1
            
            while left<right:
                three_sum=num+nums[left]+nums[right]

                if three_sum<0:
                    left+=1
                elif three_sum>0:
                    right-=1
                else:
                    res.append([num,nums[left],nums[right]])

                    left+=1
                    
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                        
        
        return res 
                