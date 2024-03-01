import collections
class ListNode:
    
    def __init__(self,left=None,val=0,right=None):
        self.left=left
        self.val=val
        self.right=right
class Solution:
#1
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
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                    
                    
        return res
    
#2    
    def twoSum(self,nums,target):
        hashset={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in hashset:
                return [hashset[diff],i]
            
            hashset[num]=i
        
        return [-1,-1]
    
#3  
    def most_container(self,height):
        
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

#4    
    def stock_buy(self,prices):
        
        max_profit=0
        
        left,right=0,0
        
        while right<len(prices):
            profit=prices[right]-prices[left]
            max_profit=max(profit,max_profit)
            if prices[left]<prices[right]:
                right+=1
            
            else:
                left=right
                right+=1
            
            
        
        return max_profit
    
#5    
    def has_duplicate(self,nums):
        numset=set()

        for num in nums:
            if num in numset:
                return True
            
            numset.add(num)
            
        return False

#6
    def has_cycle(self,head):
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
            if slow==fast:
                return True
            
        
        
        return False
    

#7    
    def reverse_linked_list(self,head):
        
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
            
        
#8    
    def merge_linked_list(self,list1,list2):
        
        temp=head=ListNode()

        
        while list1 and list2:
            
            if list1.val<list2.val:
                temp.next=list1
                list1=list1.next
                
            else:
                temp.next=list2
                list2=list2.next
                
                
            temp=temp.next
    

        temp.next = list1 or list2
        
        return head.next
    
#9    
    def validAnagram(self,word1,word2):
        charset1={}
        charset2={}

        for char in word1:
            charset1[char]=1+charset1.get(char,0)
        
        for char in word2:
            charset2[char]=1+charset2.get(char,0)

        
        return charset1==charset2
    
#10    
    def topKElements(self,nums,k):
        
        frequency_table=[[] for i in range(len(nums)+1)]
        numset={}
        res=[]
        for num in nums:
            numset[num]=1+numset.get(num,0)
        
        for num,count in numset.items():
            frequency_table[count].append(num)

        for i in range(len(frequency_table)-1,0,-1):
            for num in frequency_table[i]:
                res.append(num)
                if len(res)==k:
                    return res
   
   
#11                
    def longestSequence(self,nums):
        
        longest=0
        numset=set(nums)
        for num in numset:
            if (num-1) not in numset:
                length=1
                
                while (num+length) in numset:
                    length+=1
                
                longest=max(length,longest)
            
        return longest
    
    
#12

    def isPalindrome(self,str):
        left,right=0,len(str)-1
        
        while left<right:
            
            while not(str[left].isalpha() or str[left].isdigit()) and left<right:
                left+=1
            
            while not(str[right].isalpha() or str[right].isdigit()) and left<right:
                right-=1
            
            
            if str[left].lower()!=str[right].lower():
                return False
            
            left+=1
            right-=1
        
        return True               
    
# 13

    def longestNonRepating(self,str):
        
        charset={}

        left,right=0,0
        longest=0
        while right<len(str):
            
            if str[right] in charset:
                left=1+charset[str[right]]
                charset=0
                while left<right:
                    charset[str[left]]=left
                    left+=1
            
            
            charset[str[right]]=right
            longest=max(len(charset),longest)     
            right+=1

        return longest
                 
            

#14
    def hammingWeight(self,num):
        res=0
        while num:
            res+=num%2
            num=num>>1
        return res

# 15    
    def total_ones(self,n):
        dp=[0]*(n+1)
        offset=1
        for i in range(1,n):
            
            if offset*2==i:
                offset=i
            dp[i]=1+dp[i-offset]
        return dp
#16
    def missing(self,nums):
        missing=0
        for i in range(len(nums)):
            
            missing+=i-nums[i]
            
        return missing+len(nums)

# 17

    def rotateImage(self,matrix):
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
                
        
        for i in range(len(matrix)):
            matrix[i]=matrix[i][::-1]
        
        return matrix

    
# 18

    def spiralMatrix(self,matrix):
        
        left,right=0,len(matrix[0])
        top,bottom=0,len(matrix)
        res=[]
        while left<right and top<bottom:
            
            for i in range(left,right):
                res.append(matrix[top][i])

            top+=1
            
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
                
            right-=1
            
            if not(left<right and top<bottom):
                break
            
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            bottom-=1
            
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])

            left+=1
        return res
    
    
# 19

    def mergeIntervals(self,intervals):
        
        intervals.sort(key=lambda i: i[0])
        output=[intervals[0]]
        j=0
        for i in range(1,len(intervals)):
           
           curr_interval,prev_interval=intervals[i],output[j]
           start,end=0,1
           # [[1,5],[2,3]]
           if curr_interval[start]<=prev_interval[end]:
               max_end=max(curr_interval[end],prev_interval[end])
               output[j]=[prev_interval[start],max_end]
           else:
               output.append(intervals[i])
               j+=1
            

# 20

    def min_binary_search(self,nums):
        
        left,right=0,len(nums)-1
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

#21

    def search(self,nums,target):
        
        left,right=0,len(nums)-1
        
        while left<=right:
            
            mid=left+(right-left)//2
            
            if nums[mid]==target:
                return mid
                 
            elif nums[left]<=nums[mid]:
                if target>nums[mid] or nums[left]>target:
                    left=mid+1
                else:
                    right=mid-1
                    
            else:
                # 6,7,0,1,2, 4
                if target<nums[mid] or nums[right]<target:
                    right=mid-1
                else:
                    left=mid+1
        return -1


# 22
    def removeFromLL(self,head,n):

        if not head:
            return None
        curr=temp=head
        length=0
        while temp:
            length+=1
            temp=temp.next
        position=n-length
        if position==0:
            head=head.next
            return head

        for i in range(1,position):
            curr=curr.next
        
        deleteNode=curr.next
        
        curr.next=deleteNode.next
    
        return head
    

# 23

    def invertTree(self,root):
        
        if not root:
            return None
        
        temp=root.left
        root.left=root.right
        root.right=temp
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
# 24    
    def maxDepth(self,root):
        
        if not root:
            return 0
        
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

    def maxDepthStack(self,root):
        if not root:
            return 0
        stack=[[root,1]]
        levels=0
        while stack:
            node,depth=stack.pop()

            if node:
                levels=max(levels,depth)

                stack.append([node.left,1+depth])
                stack.append([node.right,1+depth])
            
            
        return levels
    
    
# 25
    def levelsTraversal(self,root):
        q=collections.deque()
        res=[]
        while q:
            temp=[]
            for i in range(len(q)):
                node=q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(temp)
        return res
    
    
    
# 26

    def isSameTree(self,p,q):
        if not p and not q:
            return True
        
        if not p or not q:
            return False

        if p.val!=q.val:
            return False
        
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

    
# 27
    def isSubTree(self,root,subRoot):
        
        if not subRoot:
            return True
        
        if not root:
            return False

        if self.isSameTree(root,subRoot):
            return True
        
        return self.isSubTree(root.left,subRoot)or self.isSubTree(root.right,subRoot)



            

            
        
            
print(Solution().missing([3,0,1]))
    