class Solution:
    

    def decodeWays(self,s):
        dp={len(s):1}
        def decoder(index):
            if index in dp:
                return dp[index]
            
            if s[index]=="0":
                return 0

            
            ways=decoder(index+1)

            if index<len(s)-1 and (s[index]=="1" or s[index]=="2" and s[index+1] in "0123456"):
                ways+=decoder(index+2)
            
            dp[index]=ways

            return ways

            
        
        return decoder(0)
    

    def decodeWaysIterative(self,s):
        
        dp={len(s):1}

        for i in range(len(s)-1,-1,-1):
            
            if dp[i]=="0":
                dp[i]=0
            else:
                dp[i]=dp[i+1]

            
            if i<len(s)-1 and (s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"):
                dp[i]+=dp[i+2]
            
        return dp[0]
    
    
    
    def decodeWaysRecursive(self,s):
        dp={len(s):1}
        def decoder(i):
            if i in dp:
                return dp[i] 
            
            if s[i]=="0":
                return 0

            
            ways=decoder(i+1)
            if i<len(s)-1 and (s[i]=="1" or s[i]=="2" and s[i] in "0123456"):
                ways+=decoder(i+2)
            
            dp[i]=ways
            return ways
        
        
        
        return decoder(0)
            
    
    
    def decodewaysIterative(self,s):
        dp={len(s):1}
        for i in range(len(s)-1,-1,-1):
            if dp[i]=="0":
                dp[i]=0
            else:
                dp[i]=dp[i+1]
            
            if i<len(s)-1 and (s[i]=="1" or s[i]=="2" and s[i] in "0123456"):
                dp[i]+=dp[i+2]
            
            
        return dp[0]
    

    def decodeways(self,s):
        
        dp={len(s):1}
        def decoder(index):
            
            if index in dp[index]:
                return dp[index]
            
            if dp[index]=="0":
                return dp[index]
            
            ways=decoder(index+1)

            if index<len(s)-1 and (s[index]=="1" or s[index]=="2" and s[index]+1 in "0123456"):
                ways+=decoder(index+2)
            
            dp[index]=ways
            return ways

            
        
        return decoder(0)
    
    
                


    
    def decodeWays(self,s):
        dp={len(s):1}
        def decoder(i):
            
            if i in dp:
                return dp[i]
            
            if dp[i]=="0":
                return 0
            

            ways=decoder(i+1)
            if i<len(s)-1 and (s[i]=="1" or s[i]=="2" and s[i] in "0123456"):
                ways+=decoder(i+2)
            
            dp[i]=ways
            
            return ways
        
        return decoder(0)             
    
    
    
    
    def decodeWays(self,s):
        
        dp={len(s):1}

        def decoder(i):
            
            if i in dp:
                return dp[i]
            
            if s[i]=="0":
                return 0
            
            ways=decoder(i+1)

            if i<len(s)-1 and (s[i]=="1" or s[i]=="2" and s[i] in "0123456"):
                ways+=decoder(i+2)
            
            dp[i]=ways
            return ways
            
        
        return decoder(0)
    
    
    def coinChange(self,coins,amount):
        dp=[amount+1]*(amount+1)

        dp[0]=0
        
        for amt in range(1,amount+1):
            for c in coins:
                if amt-c>=0:
                    dp[amt]=min(dp[amt],1+dp[amt-c])
        
        return dp[amt] if dp[amt] != amt+1 else -1
    
            
