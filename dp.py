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
    
    
    def climbStairs1(self,n):
        if n<=3:
            return n
        n1,n2=2,3
        
        for i in range(4,n+1):
            temp=n1+n2
            n1=n2
            n2=temp
            
        return n2
    
    def climbStairs2(self,n):
        if n<=3:
            return n
        n1,n2=2,3
        for i in range(4,n+1):
            temp=n1+n2
            n1=n2
            n2=temp
        return n2
    
    
    def climbStairs3(self,n):
        if n<=3:
            return n
        n1,n2=2,3
        
        for i in range(4,n+1):
            temp=n1+n2
            n1=n2
            n2=temp
            
        return temp
    
    
    
    def rob(self,nums):
        rob1,rob2=0,0
        
        for n in nums:
            temp=max(n+rob1,rob2)
            rob1=rob2
            rob2=temp
            
        return rob2
    
    
    def rob1(self,nums):
        rob1,rob2=0,0
        
        for num in nums:
            temp=max(num+rob1,rob2)
            rob1=rob2
            rob2=temp
        return rob2
    
    
    def rob2(self,nums):
        rob1,rob2=0,0
        
        for num in nums:
            temp=max(num+rob1,rob2)
            rob1=rob2
            rob2=temp
            
        return rob2
    def rob3(self,nums):
        rob1,rob2=0,0
        
        for num in nums:
            temp=max(num+rob1,rob2)
            rob1=rob2
            rob2=temp
            
        return rob2
    
    
    
    
    def rob4(self,nums):
        rob1,rob2=0,0
        
        for num in nums:
            temp=max(rob1+num,rob2)    
            rob1=rob2
            rob2=temp
        
        return rob2
    
    
    def helper(self,nums):
        rob1,rob2=0,0
        for num in nums:
            temp=max(rob1+num,rob2)
            rob1=rob2
            rob2=temp
            
        return rob2
    def moreRob(self,nums):
        # return max(nums[0],self.helper(nums[1:],self.helper(nums[:-1])))
        # return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))
        # return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))
        # return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))


    def countPalndrome(self,s,l,r):
        res=0
        while l>=0 and r<len(s) and s[l]==s[r]:
            res+=1
            l-=1
            r+=1
        return res
    
    
    def countSubstrings(self,s):
        res=0
        
        for i in range(len(s)):
            res+=self.countPalndrome(s,i,i)
            res+=self.countPalndrome(s,i,i+1)
        
        return res
    
    
    def helper2(self,s,l,r,res,resLen):
        while l>=0 and r<len(s) and s[l]==s[r]:
            if (r-l+1)>resLen:
                res=s[l:r+1]
                resLen=r-l+1
            
            l-=1
            r+=1
        return res,resLen
    def longestPalindrome(self,s):
        res=""
        resLen=0
        
        for i in range(len(s)):
            l,r=i,i
            res1,resLen1=self.helper2(s,l,r,res,resLen)                
            l,r=i,i+1
            self.helper2(s,l,r,res1,resLen1)

        return res
            
            
    def coinChange(self,coins,amount):
        dp=[amount+1]*(amount+1)   
        dp[0]=0

        for a in range(1,amount+1):
            for c in coins:
                if a-c>=0:
                    dp[a]=min(dp[a],1+dp[a-c])
        
        return dp[amount] if dp[amount]!=amount+1 else -1
                