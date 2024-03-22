class Solution:
    
    def climbStairs(self,n):
        
        
        def helper(curr):
            if curr>n:
                return 0
            
            if curr==n:
                return 1
            
            return helper(curr+1)+helper(curr+2)                             
        
        return helper(0)
    

print(Solution().climbStairs(5))