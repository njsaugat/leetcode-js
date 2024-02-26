class Solution:
    def best_time(self,prices):
        
        left,right=0,1
        
        max_profit=0
        
        while right<len(prices):
            
            profit=prices[right]-prices[left]
            max_profit=max(profit,max_profit)
            
            if prices[left]>prices[right]:
                
                left=right
                right+=1
            
            elif prices[left]<=prices[right]:
                right+=1
                

        
        return max_profit

print(Solution().best_time([7,1,5,3,6,4]))