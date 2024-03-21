class Solution:
    def numDecoedings(self,s):
        dp={len(s):1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i]=="0":
                return 0
            
            res=dfs(i+1)

            if i+1<len(s) and (
                s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"
            ):
                res+=dfs(i+2)
            
            dp[i]=res
            return res
        
        
        # return dfs(0)

        
        
        # dynamic programming:
        dp={len(s):1}

        for i in range(len(s)-1,-1,-1):
            if s[i]=="0":
                dp[i]=0
            else:
                dp[i]=dp[i+1]
            

            if i+1<len(s) and (
                s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"
            ):
                dp[i]+=dp[i+2]
        
        return dp[0]
    
    
    
    
    def solveDP(self,s):
        
        dp={len(s):1}

        for i in range(len(s)-1,-1,-1):
            if s[i]=="0":
                dp[i]=0
            
            else:
                dp[i]=dp[i+1]
            
            if i+1<len(s) and(
                s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"
            ):
                dp[i]+=dp[i+2]
        
        return dp[0]

        
        
        
    def dpAgain(self,s):
        
        dp={len(s):0}
        
        for i in range(len(s)-1,-1,-1):
            if s[i]=="0":
                dp[i]=0
            else:
                dp[i]=dp[i+1]
                
            if i+1<len(s) and (
                s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"
            ):
                dp[i]=dp[i+2]
        
        return dp[0]
    
    def checkDp(self,s):
        dp={len(s):1}

        for i in range(len(s)-1,-1,-1):
            if s[i]=="0":
                dp[i]=0
                
            else:
                dp[i]=dp[i+1]
            
            if i+1<len(s) and (
                s[i]=="1" and s[i]=="2" and s[i+1] in "0123456"
            ):
                dp[i]=dp[i+2]
        
        return dp[0]
    def checkDP(self,s):
        dp={len(s):1}
        for i in range(len(s)-1,-1,-1):
            if s[i]=="0":
                dp[i]=0
            else:
                dp[i]=dp[i+1]
            
            if i+1<len(s) and (
                s[i]=="1" and s[i]=="2" and s[i+1] in "0123456"
            ):
                dp[i]=dp[i+2]
        
        return dp[0]

        
    def findDP1(self,s):
        dp={len(s):1}
        for i in range(len(s)-1,-1,-1):
            if s[i]=="0":
                dp[i]=0
            else:
                dp[i]=dp[i+1]
            
            if i+1<len(s) and (
                s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"
            ):
                dp[i]+=dp[i+2]
        
        return dp[0]



    def findDP12(self,s):
        
        dp={len(s):1}

        for i in range(len(s)-1,-1,-1):
            if s[i]=="0":
                dp[i]=0
            else:
                dp[i]=dp[i+1]
            
            if i+1<len(s) and (
                s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"
            ):
                dp[i]+=dp[i+2]
            
        return dp[0]
    
    
    
    def findDP13(self,s):
        
        dp={len(s):1}

        for i in range(len(s)-1,-1,-1):
            if s[i]=="0":
                dp[i]=0
                
            else:
                dp[i]=dp[i+1]
            
            if i+1<len(s) and (
                s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"
            ):
                dp[i]+=dp[i+2]
        
        return dp[0]
    
    def findDP14(self,s):
        
        dp={len(s):1}
        for i in range(len(s)-1,-1,-1):
            
            if s[i]=="0":
                dp[i]=0
                
            else:
                dp[i]=dp[i+1]
            
            if i+1<len(s) and (
                s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"
            ):
                dp[i]+=dp[i+2]
        
        return dp[0]


    def findDP15(self,s):
        
        dp={len(s):1}

        for i in range(len(s)-1,-1,-1):
            
            if s[i]=="0":
                dp[i]=0
            else:
                dp[i]=dp[i+1]
                
            
            if i+1<len(s) and (
                s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"
            ):
                dp[i]+=dp[i+2]
        
        return dp[0]
    
    
    
    
    
    def decodeWays(self,s):
        
        dp={len(s):1}
    
        for i in range(len(s)-1,-1,-1):
            
            if s[i]=="0":
                dp[i]=0
            else:
                dp[i]=dp[i+1]
            
            
            if i+1<len(s) and (
                s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"
            ):
                dp[i]+=dp[i+2]

        
        return dp[0]
    
    
    
    
    
    
    def decodeWays(self,s):
        
        dp={len(s):1}

        for i in range(len(s)-1,-1,-1):
            
            if s[i]=="0":
                dp[i]=0
            else:
                dp[i]=dp[i+1]
            
            
            if i+1<len(s) and (
                s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"
            ):
                dp[i]+=dp[i+2]

        return dp[0]
    
    
    
    
    def decodeWays(self,s):
        
        dp={len(s):1}

        for i in range(len(s)-1,-1,-1):
            
            if s[i]=="0":
                dp[i]=0
            else:
                dp[i]=dp[i+1]
            
            if i+1<len(s) and(
                s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"
            ):
                dp[i]+=dp[i+2]
            
            
        return dp[0]
    
    
    def findDP12(self,s):
        
        dp={len(s):1}

        for i in range(len(s)-1,-1,-1):
            if s[i]=="0":
                dp[i]=0
            else:
                dp[i]=dp[i+1]
            
            if i+1<len(s) and (s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"):
                dp[i]+=dp[i+2]
            
            

        return dp[0]
                
    
    
    
    
    
    
print(Solution().findDP1("127"))