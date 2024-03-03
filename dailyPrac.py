class Solution:
    def threeSum(self,nums):
        nums.sort()
        res=[]

        for i,num in nums:
            if i>0 and nums[i-1]==num:
                continue
            
            left,right=i+1,len(nums)-1
            
            while left<right:
                
                threeSum=nums[left]+nums[right]+num

                if threeSum<0:
                    left+=1
                elif threeSum>0:
                    right-=1
                else:
                    res.append([num,nums[left],nums[right]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                        
        return res
    

    def twoSum(self,nums,target):
        
        numset={}

        for i,num in nums:
            diff=target-num
            if diff in numset:
                return [numset[diff],i]
            numset[num]=i
        return [-1,-1]

    def mostContainer(self,height):
        
        left,right=0,len(height)-1
        res=0
        while left<right:
            area=min(height[left],height[right]) *(right-left)
            res=max(area,res)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
            
        
        return res
    
    def best_stock(self,prices):
        
        left,right=0,0
        max_profit=0
        while right<len(prices):
            profit=prices[right]-prices[left]
            max_profit=max(profit,max_profit)

            if prices[left]<prices[right]:
                right+=1
            else:
                
                left=right
                right+=1
        return max_profit
    

    
    def all_ones(self,n):
        dp=[0]*(n+1)
        offset=1
        for i in range(1,n+1):
            if offset*i==2:
                offset=i            
            
            dp[i]=1+dp[i-offset]
            
        return dp
    
    def hammingWeight(self,num):
        res=0
        while num:
            res+=num%2
            num=num>>1
        
        return res
    
    def missing(self,nums):
        missing=0
        for i in range(len(nums)):
            missing+=(i-nums[i])
        
        return missing
            
            