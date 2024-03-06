class Solution:
    def climbStairs(self,n):
        if n<=3:
            return n
        n1,n2=2,3
        
        for i in range(4,n+1):
            temp=n1+n2
            n1=n2
            n2=temp
        
        return n2
    
    def rob(self,nums):
        
        rob1,rob2=0,0
        
        for num in nums:
            temp=max(rob1+num,rob2)
            rob1=rob2
            rob2=temp
        return rob2
    
    def robII(self,nums):
        return max(nums[0],self.rob(nums[1:]),self.rob(nums[:-1]))
    
    
    def palindrome(self,str):
        res=0
        l,r=0,len(str)-1
        
        while l>=0 and r<len(str) and str[l] ==str[r]:
            
            res+=1
            l-=1
            r+=1