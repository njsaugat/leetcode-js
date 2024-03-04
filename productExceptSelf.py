class Solution:
    def productExceptSelf(self,nums):
        prefix=[1]*len(nums)
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]*nums[i-1]
        
        postfix=1
        
        for i in range(len(nums)-1,-1,-1):
            prefix[i]=prefix[i]*postfix
            postfix=postfix*nums[i]

        return prefix
    
print(Solution().productExceptSelf([1,2,3,4]))