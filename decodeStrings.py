class Solution:
    
    def decodeStrings(self,s):
        # so basically what decode string means is that 
        '''
        basically the first thing to understand is if there had been 9 alphabets then the there would have been only 9 nums mapped to 9 alphabets which would make the total mappings always 1. because 123 would always have 1 2 and 3. so that would prolly have only ABC 
        but becuase we have 2 digits upto 26 that can range from 10 to 26. so this would make it kinda challenging for us.
        
        so two digits only upto 26 have to be validated.
        
        total ways t decode any string at min is one way and that would be sto simply takie in the eaach digit and map it directly
        that will always work so.
        we start of with 
        
        dp={len(s):1}
        always no matter what we start off with this line
        
        so at first if we try to create the tree then like it would follow a pattern where in we could take either 1 char or take 2 chars
        1 or 12
         
        '''
        return s
    
    i=0
    def decodeRecursive(self,s):
        
        if s=="0":
            return 0
        if len(s)==0:
            return 0
                
        if len(s)==1:
            return 1
        
        if len(s)==2:
            if s[0]=="1" or s[0]=="2" and s[1] in "0123456":
                return 1

            return 0
        
        
    
    def totalRecursive(self,s):
        res=1
        for i in range(len(s)-1,):
            # res+=self.decodeRecursive(s[i])
            res+=self.decodeRecursive(s[i:i+2])
        return res
        # return (self.decodeRecursive(s[0])+self.decodeRecursive(s[0:2]))
# ABC LC AW 







    def numDecodings(self,s):
        dp={len(s):1}
        def helper(index):
            # Base case: if the index reaches the end of the string
            # if index == len(s):
            #     return 1
            if index in dp:
                return dp[index]
            # If the current character is '0', it can't be decoded alone
            if s[index] == '0':
                return 0
            # it's like first go to the depth 
            # as you come back check if 2 strings can be processed or not
            
            ways = helper(index + 1)
            # Check if the current and next character can be decoded together
            if index < len(s) - 1 and (s[index] == '1' or (s[index] == '2' and s[index + 1] <= '6')):
                ways += helper(index + 2)
            
            dp[index]=ways
            return ways

        return helper(0)


    # def numDecodings(self,nums):
        
    #     def helper(self,nums):
    
    
    def decodeString(self,s):
        dp=[0]*(len(s)+1)
        dp[0]=1
        dp[1]=0 if s[0]=="0" else 1
        
        for i in range(2,len(s)+1):
            oneDigit=int(s[i-1:i])
            twoDigit=int(s[i-2:i])
            if oneDigit>1: 
                dp[i]+=dp[i-1]
            
            if twoDigit>=10 and twoDigit<=26:
                dp[i]+=dp[i-2]
            
        
        for i in range(2,len(s)+1):
            oneDigit=int(s[i-1:i])
            twoDigit=int(s[i-2:i])

            if oneDigit>1:
                dp[i]+=dp[i-1]
            
            if twoDigit>=10 and twoDigit<=26:
                dp[i]+=dp[i-2]

        
        for i in range(2,len(s)+1):
            oneDigit=int(s[i-1:i])
            twoDigit=int(s[i-2:i])

            if oneDigit>1:
                dp[i]+=dp[i-1]
            
            if twoDigit>=10 and twoDigit<=26:
                dp[i]+=dp[i-2]
            
            
            
        return dp[len(s)]
       
    def decodeStrings(self,s):
        # for i in range(len(s)):
            # if i in s:
        return s
    
    def findTwoSum(self,nums,target):
        numset={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in numset:
                return [numset[diff],i]
            
            numset[num]=i
        
        return [-1,-1]
    
    def findThreeSum(self,nums,target):
        
        nums.sort()

        res=[]

        for i,num in enumerate(nums):
            
            if i>0 and nums[i+1]==num:
                continue
            
            left,right=i+1,len(nums)-1
            while left<right:
                
                threeSum=num+nums[left]+nums[right]
                if threeSum>0:
                    right-=1
                elif threeSum<0:
                    left+=1
                else:
                    res.append([num,nums[left],nums[right]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                        
        
        return res
        
    def longestSequence(self,nums):
        numset=set(nums)

        for num in numset:
            if num-1 not in  numset:
                length=1
                while num+length in numset:
                    length+=1
                
                longest=max(longest,length)

        return longest

print(Solution().decodeString("123"))