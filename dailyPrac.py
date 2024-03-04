import collections

class TreeNode:
    def __init__(self,left=None,val=0,right=None):
        self.left=left
        self.val=val
        self.right=right
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution:
# 1
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
    
# 2
    def twoSum(self,nums,target):
        
        numset={}

        for i,num in nums:
            diff=target-num
            if diff in numset:
                return [numset[diff],i]
            numset[num]=i
        return [-1,-1]
# 3
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
#    4 
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
    

# 5    
    def all_ones(self,n):
        dp=[0]*(n+1)
        offset=1
        for i in range(1,n+1):
            if offset*i==2:
                offset=i            
            
            dp[i]=1+dp[i-offset]
            
        return dp
#    6 
    def hammingWeight(self,num):
        res=0
        while num:
            res+=num%2
            num=num>>1
        
        return res
    # 7
    def missing(self,nums):
        missing=0
        for i in range(len(nums)):
            missing+=(i-nums[i])
        
        return missing
        
    # 8
    def longestSequence(self,nums):
        
        numset=set(nums)
        longest=0
        for num in nums:
            
            if (num-1) not in numset:
               length=1
               while (num+length) in numset:
                   length+=1
                 
               longest=max(length,longest)
            
        return longest
    
    
    #  9
    def kMostRepeated(self,nums,k):
        
        freq_table=[[] for i in range(len(nums+1))]
        numset={}
        res=[]
        for num in nums:
            numset[num]=1+nums.get(num,0)
        
        for num,count in numset.items():
            freq_table[count].append(num)

        
        for i in range(len(freq_table)-1,0,-1):

            for num in freq_table[i]:
                res.append(num)    
                if len(num)==k:
                    return res
                
    
    # 10
    def mostLongestSubstring(self,str):
        
        charset={}

        left,right=0,0
        longest=0
        while right<len(str):
            
            if str[right] in charset:
                
                left=1+charset[str[right]]

                charset={}

                while left<right:
                    charset[str[left]]=left
                    left+=1
                        
            charset[str[right]]=right
            longest=max(longest,len(charset))
            right+=1

        return longest
            
    
        #11
        
    def hasCycle(self,head):
        
        slow,fast=head,head 

        while fast and fast.next:
            
            slow=slow.next
            fast=fast.next.next
            
            if slow==fast:
                return True
        return False
    
    # 12
    
    def mergeLists(self,list1,list2):
        temp=head=ListNode()

        while list1 and list2:
            
            if list1.val<list2.val:
                temp.next=list1
                list1=list1.next
                
            else:
                temp.next=list2
                list2=list2.next
                
            temp=temp.next
            
        
        temp.next=list1 or list2
        
        return head.next
    
    # 13
    
    def reverseList(self,head):
        
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
                
#14

    def deleteNode(self,head,n):
        curr=temp=head
        length=0
        while temp:
            length+=1
            temp=temp.next
        
        position=length-n
        if position==0:
            head=head.next
            return head
        
        for i in range(1,position):
            curr=curr.next
        
        deleteNode=curr.next        
        curr.next=deleteNode.next
        
        return head

# 15
    def spiralMatrix(self,matrix):
        res=[]

        left,right=0,len(matrix[0])
        top,bottom=0,len(matrix)

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
            
            for i in range(bottom-1,top,-1):
                res.append(matrix[i][left])
            left+=1
        return res
    
    # 16
    
    def rotateImage(self,matrix):
        
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
                
        
        for i in range(len(matrix)):
            matrix[i]=matrix[i][::-1]
        return matrix

    # 17
    def mergeIntervals(self,intervals):
        intervals.sort(key=lambda i: i[0])

        output=[intervals[0]]
        j=0
        for i in range(1,len(intervals)):

            curr_interval,prev_interval=intervals[i],output[j]

            start,end=0,1
            
            if curr_interval[start]<= prev_interval[end]:
                max_end=max(curr_interval[end],prev_interval[end])
                output[j]=[prev_interval[start],max_end]
            
            else:
                output.append(intervals[i])
                j+=1
        return output
    
    
    # 18
    def hasDuplicate(self,nums):
        numset=set()

        for num in nums:
            
            if num in numset:
                return True
            numset.add(num)
            
        return False
    
    # 19
    def validAnagram(self,word1,word2):
        
        charset1={}
        charset2={}

        for char in word1:
            charset1[char]=1+charset1.get(char,0)
        for char in word2:
            charset2[char]=1+charset2.get(char,0)

        return charset1==charset2
    
    
    # 20
    
    def isPalindrome(self,str):
        left,right=0,len(str)-1
        if len(str)==0:
            return True
        if len(str)==1:
            return False
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
    
    
    # 21
    
    def minimum(self,nums):
        
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
                
                if nums[left]>nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return min(curr_min,nums[left])
    
    
    # 22
    def search(self,nums,target):
        
        left,right=0,len(nums)-1
        
        while left<=right:
            mid=left+(right-left)//2
            
            if nums[mid]==target:
                return mid
            
            elif nums[left]<=left[mid]:
                if target>nums[mid] or target<nums[left]:
                    left=mid+1
                else:
                    right=mid-1
            
            else:
                if target<nums[mid] or target>nums[right]:
                    right=mid-1
                else:
                    left=mid+1
                    
        return -1
    
    
    
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
                stack.append([stack.left,1+depth])
                stack.append([stack.right,1+depth])
        
        return levels
    
    
    # 25
    def levelsOrder(self,root):
        q=collections.deque([root])

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
    def isSubTree(self,tree,subTree):
        
        if not subTree:
            return True
        
        if not tree:
            return False
        
        if self.isSameTree(tree,subTree):
            return True
        
        return self.isSubTree(tree.left,subTree) or self.isSubTree(tree.right,subTree)
    
    
    # 28
    def groupAnagrams(self,words):
        output={}
        res=[]
        for word in words:
            
            
            letters=[0]*26
            
            for char in word:
                diff=ord(char)-ord('a')
                letters[diff]+=1
            
            
            
            output[repr(letters)]=output.get(repr(letters),[])
            output[repr(letters)].append(word)
        
        return [value for key,value in output.items()]


    def productExceptSelf(self,nums):
        output=[1]*len(nums)    

        for i in range(len(nums)):
            output[i]=output[i-1]*nums[i-1]
        
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            # 12, 8, 6
            output[i]=output[i]*postfix
            postfix=postfix*nums[i]
            
        return output


print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))