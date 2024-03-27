class Solution:
    
    def longestCommonPrefix(self,strs):
        
        common=''
        
        def findCommon(word1,word2):
            currCommon=''
            for j in range(min(len(word1),len(word2))):
                if currWord[j]!=nextWord[j]  :
                    break
                currCommon+=currWord[j]
            return currCommon
        
        for i in range(len(strs)-1):
            currWord,nextWord=strs[i],strs[i+1]
            currCommon=findCommon(currWord,nextWord)
            
            if i==0:
                common=currCommon
            else:            
                common=findCommon(currCommon,common)
        
        return common
            
            
    
    
    def findMinCoinChange(self,amount,coins):
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for amt in range(1,amount+1):
            for coin in coins:
                if amt>=coin:
                    dp[amt]=min(dp[amt],1+dp[amt-coin])
                
                
        return dp[amount] if dp[amount]!=amount+1 else -1
    
    def findMinCoins(self,coins,amount):
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for amt in range(1,amount+1):
            for coin in coins:
                if amt>=coin:
                    dp[amt]=min(dp[amt],1+dp[amt-coin])
        
        return dp[amount] if dp[amount]!=amount+1 else -1
    
    
    

    def sortColors(self,nums):
        
        left,mid,right=0,0,len(nums)-1
        
        while mid<=right:
            
            if nums[mid]==0:
                nums[left],nums[mid]=nums[mid],nums[left]
                left+=1
                mid+=1
            
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[right]=nums[right],nums[mid]
                right-=1
        
        return nums
print(Solution().longestCommonPrefix(["flower","flow","flight"]))     
            