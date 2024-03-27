class Solution:
    
    def findMaxProfitInSack(self,weights,profits,maxWeight):
        weights.insert(0,0)
        profits.insert(0,0)
        n=len(weights)
        m=maxWeight
        knapsack=[[0 for _ in range(m+1)] for _ in range(n)]
        for i in range(n):
            for w in range(m+1):
                
                if i==0 or w==0:
                    knapsack[i][w]=0
                    
                elif  weights[i]<=w:
                    knapsack[i][w]=max(profits[i]+knapsack[i-1][w-weights[i]],knapsack[i-1][w])
                else:
                    knapsack[i][w]=knapsack[i-1][w]
        
        
        return knapsack[n-1][w]


print(Solution().findMaxProfitInSack([2,3,4,5],[1,2,5,6],8))