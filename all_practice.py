class Solution:
    def threeSum(self,nums):
        nums.sort()
        res=[]

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
                    l+=1
                    while nums[left-1]==nums[left] and left<right:
                        l+=1
        return res
    
    def twoSum(self,nums,target):
        hashset={}
        for i,num in enumerate(nums):
            
            diff=target-num
            if diff in nums:
                return [hashset[diff],i]
            
            hashset[num]=i
        return [-1,-1]
    
    
    def spiral_matrix(self,matrix):
        
        left,right=0,len(matrix[0])
        top,bottom=0,len(matrix)
        res=[]
        while top<bottom and left<right:
            
            for i in range(left,right):
                res.append(matrix[top][i])
            top+=1
            
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right-=1
            
            if not (top<bottom and left<right):
                break
            
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            
            bottom-=1
            
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
                
            left+=1
        
        return res
    
    
    def most_container(self,height):
        left,right=0,len(height)-1
        res=0
        while left<right:
            area=min(height[left],height[right])*(right-left)
            res=max(res,area)
            
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
            
        return res
    
    def stock_buy(self,prices):
        
        left,right=0,0
        max_profit=0
        while right<len(prices):
            profit=prices[right]-prices[left]
            max_profit=max(profit,max_profit)

            if prices[left]<=prices[right]:
                right+=1
            elif prices[left]>prices[right]:
                left=right
                right+=1
            
        return max_profit
    
    def hammingWeight(self,num):
        res=0
        while num:
            res+=num%2
            num=num>>1
        
        return res
    def total_ones(self,n):
        dp=[0]*(n+1)
        offset=1
        for i in range(1,n+1):
            if offset*2==i:
                offset=i
            dp[i]=1+dp[i-offset]
            
        return dp
    
    def missing(self,nums):
        n=len(nums)
        missing=sum=(n*(n+1))//2

        for num in nums:
            missing-=num
        return missing
    
    def rotate_image(self,matrix):
        
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
            
        
        for i in range(len(matrix)):
            matrix[i]=matrix[i][::-1]
        
        return matrix
    
    def has_duplicate(self,nums):
        numset=set()
        for num in nums:
            if num in numset:
                return True
            numset.add(num) 
        
        return False
    
    def is_anagram(self,word1,word2):
        
        hashset1={}
        hashset2={}

        for char in word1:
            hashset1[char]=1+hashset1.get(char,0)

        for char in word2:
            hashset2[char]=1+hashset2.get(char,0)
        
        return hashset1==hashset2
    
    
    def topKElements(self,nums,k):
        
        frequency_table=[[]for i in range(len(nums)+1)]
        numset={}
        res=[]
        for num in nums:
            numset[num]=1+numset.get(num,0)

        for num,count in numset.items():
            frequency_table[count].append(num)
            
        for i in range(len(frequency_table)-1,0,-1):
            for num in frequency_table[i]:
                res.append(num)
                if len(nums)==k:
                    return res
                
        
    
    def longestSequence(self,nums):
        numset=set(nums)# remove duplicates
        longest=0
        for num in numset:
            # start of a sequence
            if (num-1) not in numset:
                
                length=1
                while (num+length) in numset:
                    length+=1
                    
                longest=max(length,longest)
        
        return longest
    
    def isPalindrome(self,s):
        if len(s)==0:
            return False
        if len(s)==1:
            return True
        left,right=0,len(s)-1 
        while left<right:
            
            while not( s[left].isalpha() or s[left].isdigit() ) and left<right:
                left+=1
                
            while not( s[right].isalpha() or s[right].isdigit() ) and left<right:
                right-=1
                

            
            if s[left].lower()!=s[right].lower():
                return False
        
            left+=1
            right-=1    
        
        return True
                
    
    def longestSubstring(self,str):
        charset={}
        left,right=0,0
        if len(str)==0:
            return 0
        longest=1
        
        while right<len(str):
            
            if str[right] in charset:
                left=1+charset[str[right]]
                
                charset={}

                while left<right:
                    charset[str[left]]=left
                    left+=1
            # charset.add()               
            charset[str[right]]=right
            longest=max(longest,len(charset))
            right+=1
        
        return longest
      
    
    def has_cycle(self,head):
        
        slow,fast=head,head          

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
    
    def reverseLinkedList(self,head):
        p=None
        q=head
        r=head.next
        
        while q:
            q.next=p
            p=q
            q=r
            if r:
                r=r.next
            
        return p
    
    
    def mergeintervals(self,intervals):
        
        intervals.sort(key=lambda i:i[0])

        output=[intervals[0]]
        j=0
        for i in range(1,len(intervals)):
            
            current_interval,prev_interval=intervals[i],output[j]

            start,end=0,1
            
            if current_interval[start]<=prev_interval[start]:
                max_end=max(current_interval[end],prev_interval[end])
                output[j]=[prev_interval[start],max_end]
            else:
                output.append(intervals[i])
                j+=1
        
        return output

    
    def min_sorted(self,nums):
        left,right=0,len(nums)-1
        
        
        if nums[left]<nums[right]:
            return nums[left]
        curr_min=float("infinity")
        while left<right:
            mid=left+(right-left)//2
            curr_min=min(curr_min,nums[mid])
            
            if nums[left]<=nums[mid]:
                if nums[left]<nums[right]:
                    right=mid-1
                else:
                    left=mid+1 
            else:
                if nums[left]<nums[right]:
                    left=mid+1
                else:
                    right=mid-1
                
        return min(curr_min,nums[left])
        
    
    def search(self,nums,target):
        
        
        left,right=0,len(nums)-1
        
        while left<=right:
            mid=left+(right-left)//2
            
            if nums[mid]==target:
                return mid
            # left sorted
            if nums[left]<=nums[mid]:
                if nums[left]>target or target>nums[mid]:
                    left=mid+1
                else :
                    right=mid-1
            else:
                if nums[right]<target or target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
        return -1
        # while left<right:   
        #     mid=
            
            
    def most_repeating(self,str,k):
        charset={}

        for char in str:    
            charset[char]=1+charset.get(char,0)
        
        return charset

    
    
    def search_rotated(self,nums,target):
        
        left,right=0,len(nums)-1
        
        while left<=right:
            mid=left+(right-left)//2
            
            if nums[mid]==target:
                return mid
            
            # left sorted position
            # 4,5,6,7,0,1,2
            # 7,0,1,2,4,5,6,
            elif nums[left]<=nums[mid]:

                if target>nums[mid] or nums[left]>target:
                    left=mid+1 
                else:
                    right=mid-1
            else:
                if target<nums[mid] or nums[right]<target:
                    right=mid-1
                else:
                    left=mid+1
        
        return -1
print(Solution().most_repeating("ABABBBA",1))