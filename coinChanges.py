class Solution:
    
    def coinChangeRecursive(self,amount,coins):
        def exchanger(amount,coin):
            
            
            if amount==0:
                return 0
            if amount<0:
                return -1

            if amount<coin:
                return -1
            
            value1=exchanger(amount,coins[0])
            
            if value1<0:
                return -1
            
            value2=exchanger(amount,coins[1])
            
            if value2<0:
                return -1
            
            min(value,value221)
            return 1+value1
        
        return exchanger(amount,coins[0])



    def coinChangeIterative(self,amount,coins):
        
        dp=[amount+1]*(amount+1)
        dp[0]=0
        
        for amt in range(1,amount+1):
            for coin in coins:
                if amt-coin>=0:
                    dp[amt]=min(dp[amt],1+dp[amt-coin])
            
        return dp[amount] if dp[amount]!=amount+1 else -1
        

print(Solution().coinChangeIterative(14,[2,5]))