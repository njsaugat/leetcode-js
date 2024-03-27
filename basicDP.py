

class DP:
    
    def fibonacciR(self,n):
        if n<=1:
            return n
        
        return self.fibonacciR(n-2)+self.fibonacciR(n-1)
    
    
    def fibonacciMemo(self,n):
        memo={}
        def fib(n):
            if n<=1:
                return n
            if n in memo:
                return memo[n]
            
            memo[n]=fib(n-2)+fib(n-1)
            return memo[n]
        
        return fib(n)
    def fibonacciMemoArray(self,n):
        memo=[-1]*(n+1)
        def fib(n):
            if n<=1:
                return n
            if memo[n]!=-1:
                return memo[n]
            
            memo[n]=fib(n-2)+fib(n-1)
            return memo[n]
        
        return fib(n)
    
    
    def fibonacciTabulation(self,n):
        if n<=1:
            return n
        dp=[0]*(n+1)

        dp[0]=0
        dp[1]=1
        
        for i in range(2,n+1):
            dp[i]=dp[i-2]+dp[i-1]
    
        return dp[n]
        
    
    def fibonacciTabulation(self,n):
        
        if n<=1:
            return n
        
        dp=[0]*(n+1)
        
        dp[0]=0
        dp[1]=1
        
        for i in range(2,n+1):
            dp[i]=dp[i-2]+dp[i-1]
        
        return dp[n]
        
    
print(DP().fibonacciTabulation(200))