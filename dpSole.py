class Solution:
    
    def staircase(self,n):
        
        n1,n2=0,1
        
        for i in range(1,n):
            temp=n1+n2
            n1=n2
            n2=temp
        return n2
    
    
    def rob(self,nums):
        
        rob1,rob2=0,0
        
        for num in nums:
            newRob=max(rob1+num,rob2)
            rob1=rob2
            rob2=newRob
            
        return rob2
    
    def maxRob(self,nums):
        
        if len(nums)==0:
            return nums[0]
        
        return max(self.rob(nums[1:]),self.rob(nums[:-1]))
    
    
    def totalPalindromes(self,s):
        res=0
        for i in range(len(s)):
            
            res+=self.countPalindrome(s,i,i)
            res+=self.countPalindrome(s,i,i+1)

    
        return res    
    def countPalindrome(self,s,l,r):
        
        res=0
        # we are not creating a substring
        # instead we are moving serially and assuming each letter to be the center
        while l>=0 and r<len(s) and s[l]==s[r]:
            res+=1
            l-=1
            r+=1
        
        return res
    
    
    
    def longestSubstring(self,s):
        
        res=''        
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1>len(res)):
                    res=s[l:r+1]
                l-=1
                r+=1
                    
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1>len(res)):
                    res=s[l:r+1]
                l-=1
                r+=1
                
        return res

print(Solution().longestSubstring("babad"))
            
            
                 
                