class Solution:
    
    def total_ones(self,n):
        
        dp=[0]*(n+1)
        offset=1
        for num in range(1,n+1):
            
            if offset*2==num:
                offset=num 
            
            dp[num]=1+dp[num-offset]
            
            
        return dp