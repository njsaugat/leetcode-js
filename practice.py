class Solution:
    def threesum(self,nums):
        # left,right=    
        res=[]
        nums.sort()

        for i,num in enumerate(nums):
            if i>0 and nums[i-1]==num:
                continue

            left,right=i+1,len(nums)-1
            
            while left<right:
                threeSum=num+nums[left]+nums[right]

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
    
    def most_water(self,height):
        
        left,right=0,len(height)-1
        res=0
        while left<right:
            area=min(height[left],height[right])*(right-left)
            res=max(area,res)
            
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
            
        return res
            
                
    def total_ones(self,num):
        
        res=0
        while num:
            res+=num%2
            num=num>>1
        
        return res
    
    def total_ones_count(self,n):
        dp=[0]*(n+1)
        offset=1
        for num in range(1,n+1):
            if offset*2==num:
                offset=num
            
            dp[num]=1+dp[num-offset]
            
        return dp
            
            
    def topKelements(self,nums,k):
        
        hashset={}
        frequency_table=[[] for i in range(len(nums)+1)]
        res=[]
        for num in nums:
            hashset[num]=1+hashset.get(num,0)
        
        for num,count in hashset.items():
            frequency_table[count].append(num)
        
        for i in range(len(frequency_table)-1,0,-1):
            for frequency in frequency_table[i]:
                res.append(frequency)
                if len(res)==k:
                    return res
                
    
    