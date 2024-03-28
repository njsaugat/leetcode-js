class Solution:
    
    def maxProduct(self,nums):
        
        res=nums[0]
        curMin,curMax=1,1
        
        for n in nums:
            temp=curMax*n
            curMax=max(n*curMax,n*curMin,n)
            curMin=min(temp,n*curMin,n)
            res=max(res,curMax)
        
        return res
    
    def maxProduct(self,nums):
        
        res=nums[0]
        curMin,curMax=1,1

        for n in nums:
            temp=curMax*n
            curMax=max(n*curMax,n*curMin,n)
            curMin=min(temp,n*curMin,n)
            res=max(res,curMax)
        
        return res
    
    
    def maxProduct(self,nums):
        
        res=nums[0]

        curMin,curMax=1,1
        
        for n in nums:
            temp=curMax*n
            curMax=max(n*curMax,n*curMin,n)
            curMin=min(temp,n*curMin,n)

            res=max(res,curMax)
        
        return res
    
    
    def maxProduct(self,nums):
        
        res=nums[0]

        curMin,curMax=1,1
        
        for num in nums:
            temp=curMax*num
            curMax=max(num*curMax,num*curMin,num)
            curMin=min(temp,num*curMin,num)
            res=max(res,curMax)
        
        return res
    
    
    def maxProduct(self,nums):
        
        res=nums[0]
        curMin,curMax=1,1
        
        for num in nums:
            
            temp=curMax*num
            
            curMax=max(num*curMax,num*curMin,num)
            curMin=min(temp,num*curMin,num)
            res=max(res,curMax)
        
        return res
    
    def maxProduct(self,nums):
        
        res=nums[0]

        curMin,curMax=1,1
        
        for num in nums:
            temp=curMax*num
            
            curMax=max(num*curMax,num*curMin,num)
            curMin=min(temp,curMin*num,num)
            res=max(res,curMax)
        
        return res
    
    
    def maxProduct(self,nums):
        res=nums[0]
        curMin,curMax=1,1

        for num in nums:
            
            temp=num*curMax

            curMax=max(num*curMax,num*curMin,num)
            curMin=min(temp,num*curMin,num)
            res=max(res,curMax)
            
        return res
            
    
    def maxProduct(self,nums):
        
        curMax,curMin=1,1
        res=nums[0]
        for num in nums:
            
            temp=num*curMax
            curMax=max(curMax*num,curMin*num,num)
            curMin=min(temp,curMin*num,num)
            res=max(res,curMax)
        return res
    
    
    
    def maxProduct(self,nums):

        res=nums[0]
        curMin,curMax=1,1
        
        for num in nums:
            
            temp=curMax*num
            curMax=max(num*curMax,num*curMin,num)
            curMin=min(temp,num*curMin,num)
            res=max(curMax,res)
        
        return res
    
    
    
    def maxProducts(self,nums):
        curMin,curMax=1,1
        res=nums[0]
        for num in nums:
            
            temp=curMax*num
            curMax=max(num*curMin,num*curMax,num)
            curMin=min(temp,num*curMin,num)
            res=max(res,curMax)
        
        return res
    
    
    
    
    def maxProducts(self,nums):
        curMin,curMax=1,1
        res=nums[0]
        for num in nums:
            temp=num*curMax
            curMax=max(num*curMax,num*curMin,num)
            curMin=max(temp,num*curMin,num)
            res=max(curMax,res)
        
        return res
    
    
    
        
    
            
            
        
          
            
            
        