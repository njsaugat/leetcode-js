class Solution:
    
    def coinChange(self,amount,coins):

        dp=[amount+1]*(amount+1)
        dp[0]=0
        
        for amt in range(1,amount+1):
            for coin in coins:
                if amt>=coin:
                    dp[amt]=max(dp[amt],1+dp[amt-coin])
        
        
        return dp[amount] if dp[amount]!=amount+1 else -1
    
    def maxProduct(self,nums):
        
        curMin,curMax=1,1
        
        res=nums[0]
        for num in nums:
            temp=num*curMax
            curMax=max(num*curMax,num*curMin,num)
            curMin=min(temp,num*curMin,num)

            res=max(res,curMax)
        
        return res
    
    def findLIS(self,nums):
        LIS=[1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                
                if nums[i]<nums[j]:
                    LIS[i]=max(LIS[i],1+LIS[j])
            
        return max(LIS)
    
    
    
    def partitionSum(self,nums):
        
        if sum(nums)%2:
            return False
        
        dp=set()
        dp.add(0)

        target=sum(nums)%2
        
        for i in range(len(nums)-1,-1,-1):
            nextDP=set()
            for t in dp:
                
                if (t+nums[i])==target:
                    return True

                nextDP.add(t+nums[i])
                nextDP.add(t)
                
            dp=nextDP

        return False
            
    
    def wordBreak(self,s,wordDict):
        dp=[False]*(len(s)+1)        
        dp[len(s)]=True
        
        
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                
                if (i+len(w)<=len(s)) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                
                if dp[i]:
                    break
                
        return dp[0]
    
    
    def wordBreak(self,s,wordDict):
        dp=[False]*(len(s)+1)
        dp[len(s)]=True
        
        for i in range(len(s)-1,-1,-1):
            
            for w in wordDict:
                if (i+len(w)<=len(s) ) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                
                if dp[i]:
                    break
                
        return dp[0]
        
    
    
    def breakWord(self,s,wordDict):
        
        dp=[False] *(len(s)+1)    
        dp[len(s)]=True
        
        for i in range(len(s)-1,-1,-1):
            
            for w in wordDict:
                if (i+len(w)<=len(s)) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                if dp[i]:
                    break
            
        return dp[0]



    def breakWord(self,s,wordDict):
        
        dp=[False]*(len(s)+1)

        dp[len(s)]=True
        
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i+len(w)<=len(s)) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
        
        
                if dp[i]:
                    break
                
        
        return dp[0]


    
    def breakWord(self,s,wordDict):
        
        dp=[False]*(len(s)+1)
        dp[len(s)]=True
        for i in range(len(s)-1,-1,-1):
            
            for w in wordDict:
                if (i+len(w)<=len(s)) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                if dp[i]:
                    break
        
        return dp[0]


    def breakWord(self,s,wordDict):
        
        dp=[False]*(len(s)+1)

        dp[len(s)]=True
        
        for i in range(len(s)-1,-1,-1):
            
            for w in wordDict:
                
                if (i+len(w)<=len(s)) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                if dp[i]:
                    break
        
        return dp[0]
    
    
    
    def breakWord(self,s,wordDict):
        
        dp=[False]*(len(s)+1)

        dp[len(s)]=True
        
        
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                
                if (i+len(w)<=len(s)) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                if dp[i]:
                    break
                
        
        return dp[0]

    
    
    
    def breakWord(self,s,wordDict):
        
        dp=[False]*(len(s)+1)
        dp[len(s)]=True
        
        
        for i in range(len(s)-1,-1,-1):
            
            for w in wordDict:
                
                if (i+len(w)<=len(s)) and  s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]

                if dp[i]:
                    break
        
        return dp[0]
            
        
            
                
        

    
    def breakWord(self,wordDict,s):
        
        dp=[False]*(len(s)+1)

        dp[len(s)]=True
        
        
        for i in range(len(s)-1,-1,-1):
            
            for w in wordDict:
                
                if (i+len(w)<=len(s)) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                
                if dp[i]:
                    break
            
            
        return dp[0]



    
    def breakWord(self,wordDict,s):
        
        dp=[False]*(len(s)+1)

        dp[len(s)]=True
        
        for i in range(len(s)-1,-1,-1):
            
            for w in wordDict:
                
                if (i+len(w)<=len(s)) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                if dp[i]:
                    break
                
        
        return dp[0]
    
    
    def breakWord(self,s,wordDict):
        
        dp=[False]*(len(s)+1)
        
        dp[len(s)]=True
        
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                
                if (i+len(w)<=len(s)) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]

                if dp[i]:
                    break
                
        
        return dp[0]
    
    
    def breakWord(self,s,wordDict):
        
        dp=[False]*(len(s)+1)
        dp[len(s)]=True
        
        for i in range(len(s)-1,-1,-1):
            
            for w in wordDict:
                
                if (i+len(w)<=len(s)) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                if dp[i]:
                    break
        
        return dp[0]
    
    def breakWord(self,s,wordDict):
        
        dp=[False]*(len(s)+1)

        dp[len(s)]=True
        
        for i in range(len(s)-1,-1,-1):
            
            for w in wordDict:
                if (i+len(w)<=len(s)) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                
                if dp[i]:
                    break
                
        return dp[0]

    
    def breakWord(self,wordDict,s):
        
        dp=[False]*(len(s)+1)
        dp[len(s)]=True
        for i in range(len(s)-1,-1,-1):
            
            for w in wordDict:
                if (s+len(w)<=len(s)) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                
                if dp[i]:
                    break
            
            
        return dp[0]

    
    def findLIS(self,nums):
        
        LIS=[1]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            
            for j in range(i+1,len(nums)):
                
                if nums[i]<nums[j]:
                    LIS[i]=max(LIS[i],1+LIS[j])
        
        
        return max(LIS)

    
    def partitionSum(self,nums):
        
        if sum(nums)%2:
            return False
        
        dp=set()
        dp.add(0)
        target=sum(nums)//2
        for i in range(len(nums)-1,-1,-1):
            nextDP=set()
            for t in dp:
                
                if (t+nums[i])==target:
                    return True
                nextDP.add(t+nums[i])
                nextDP.add(t)
                
            
            dp=nextDP
        
        return False
    
    def partitionSum(self,nums):
        
        if sum(nums)%2:
            return False
        
        
        dp=set()
        dp.add(0)

        target=sum(nums)//2
        for i in range(len(nums)-1,-1,-1):
            nextDP=set()

            for t in dp:
                
                if (t+nums[i])==target:
                    return True 
                
                nextDP.add(t+nums[i])    
                nextDP.add(t)    
            
            dp=nextDP
                    

        return False
    
    
    def wordBreak(self,wordDict,s):
        
        dp=[False]*(len(s)+1)
        dp[len(s)]=True
        for i in range(len(s)-1,-1,-1):
            
            for w in wordDict:
                
                if (i+len(w)<=len(s)) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                
                if dp[i]:
                    break
            
            
        return dp[0]
    
                
                    
        
        
            