class Solution:
    # memo={}
    def fibonacci(self,num):
        memo={}
        def helper(num):
            if num in memo:
                return memo[num]
            if num<=1:
                return num
        
            memo[num]=helper(num-1)+helper(num-2)
            return memo[num]
        
        
        value= helper(num)
        print(memo)
        return value
    


print(Solution().fibonacci(100))