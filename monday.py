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
    
    def twoSum(self,nums,target):
        numset={}

        for i,num in enumerate(nums):
            diff=target-num
            if diff in numset:
                return [numset[diff],i]
            numset[num]=i
            
        return [-1,-1]
    
    def hasDuplicate(self,nums):
        numset=set()

        for num in nums:
            if num in numset:
                return True
            
            numset.add(num)
            
        return False
    
    def validAnagram(self,word1,word2):
        charset1={}
        charset2={}
        for char in word1:
            charset1[char]=charset1.get(char,0)
        
        for char in word2:
            charset2[char]=charset2.get(char,0)
        
        return charset1==charset2
    
    def topKElements(self,nums,k):
        frequency_table=[[] for i in range(len(nums)+1)]

        res=[]
        numset={}

        for num in nums:
            numset[num]=1+numset.get(num,0)
        
        for num,count in numset.items():
            frequency_table[count].append(num)

        for i in range(len(frequency_table)-1,0,-1):
            
            for num in frequency_table[i]:
                res.append(num)
                if len(res)==k:
                    return res
                
    
    def groupAnagrams(self,words):
        
        output={}

        for word in words:
            
            letters=[0]*26
            for char in word:
                
                diff=ord(char)-ord("a")
                letters[diff]+=1
            
            key=repr(letters)
            output[key]=output.get(key,[])
            output[key].append(word)
            
        
        return [value for key,value in output.items()]
    
    def longestSequence(self,nums):
        numset=set(nums)
        longest=0
        for num in numset:
            
            if num-1 not in numset:
                length=1
                while (num+length) in numset:
                    length+=1
                    
                longest=max(longest,length)
        
        return longest
    
    def productExceptSelf(self,nums):
        
        output=[1]*len(nums)
        for i in range(1,len(nums)):
            output[i]=output[i-1]*nums[i-1]
            
        postfix=1
        
        for i in range(len(nums)-1,0,-1):
            output[i]=output[i]*postfix
            postfix=postfix*nums[i]
            
        return output
    # dup,ana,2,valid,product,longest,topk
    def mostContainer(self,height):
        left,right=0,len(height)
        res=0
        while left<right:

            area=min(height[left],height[right])*(right-left)
            res=max(area,res)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
                
        return res
    
    def validPalindrome(self,str):
        
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


    def bestStock(self,prices):
        
        max_profit=0
        
        left,right=0,0
        
        while right<len(prices):
            profit=prices[right]-prices[left]
            max_profit=max(profit,max_profit)

            if prices[left]<prices[right]:
                right+=1
            else:
                left=right
        
        return max_profit
             
             
    
    def longestCharSequence(self,str):
        
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
    
    def hasCycle(self,head):
        slow,fast=head,head
        
        while fast and fast.next:
            
            slow=slow.next
            fast=fast.next.next
            
            if slow==fast:
                return True
            
        
        return False
    
    def mergeSortedLists(self,list1,list2):
        
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
    
    def removeFromList(self,head,n):
        
        temp=curr=head
        length=0
        while temp:
            length+=1
            temp=temp.next
        
        position=length-0
        if position==0:
            head=head.next
            return head
            
        for i in range(1,position):
            curr=curr.next
            
        deleteNode=curr.next
        
        curr.next=deleteNode.next
        
        return head
    
    
    
    def search(self,nums,target):
        
        left,right=0,len(nums)-1
        
        while left<=right:
            
            mid=left+(right-left)//2
            
            if nums[mid]==target:
                return mid
            
            elif nums[left]<=nums[mid]:
                
                if target<nums[left] or target>nums[mid]:
                    left=mid+1
                else:
                    right=mid-1
                
            else:
                if target>nums[right] or target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
                    
        return -1
    
    def minSorted(self,nums):
        
        left,right=0,len(nums)-1
        curr_min=float("-infinity")
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

    
    def rotateImage(self,matrix):
        
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
                
        
        for i in range(len(matrix)):
            matrix[i]=matrix[i][::-1]
            
        return matrix
    
    def spiralMatrix(self,matrix):
        
        top,bottom=0,len(matrix)
        left,right=0,len(matrix[0])
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
    
    def mergeIntervals(self,intervals):
        intervals.sort(key=lambda i:i[0])
        output=[intervals[0]]
        j=0
        for i in range(1,len(intervals)):
            curr_interval,prev_interval=intervals[i],output[j]
            start,end=0,1
            
            if curr_interval[start]<=prev_interval[end]:
                max_end=max(curr_interval[end],prev_interval[end])
                output[j]=[prev_interval[start],max_end]
            else:
                output.append(intervals[i])
                j+=1

        return output
    
    def invertTree(self,root):
        if not root:
            return None
        
        temp=root.left
        root.left=root.right
        root.right=temp
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
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

                stack.append([root.left,1+depth])
                stack.append([root.right,1+depth])
            
        return levels
    
    
    def isSameTree(self,p,q):
        
        if not p and not q:
            return True
        
        if not p or not q:
            return False

        if p.val!=q.val:
            return False

        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    
    def isSubTree(self,tree,subTree):
        if not subTree:
            return True
        
        if not tree:
            return False
        
        if self.isSameTree(tree,subTree):
            return True
        
        return self.isSubTree(tree.left,subTree) or self.isSubTree(tree.right,subTree)

    
    def levelOrder(self,root):
        res=[]
        q=collections.deque([root])

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
    
    
    def lowestCommonAncestor(self,root,p,q):
        
        while True:
            
            if root.val<p.val and root.val<q.val:
                root=root.right
            elif root.val>p.val and root.val>q.val:
                root=root.left
            else:
                return root
            
    def smallestKBSt(self,root,k):
        
        stack=[]
        curr=root
        while stack or curr:
            
            while curr:
                stack.append(curr)
                curr=curr.left
            
            curr=stack.pop()

            k-=1
            if k==0:
                return curr.val
            
            curr=curr.right
    
    
    def missingNumber(self,nums):
        missing=0
        for i in range(len(nums)):
            missing+=(i-nums[i])   
        return missing
    
    def hammingWeight(self,n):
        res=0
        while n:
            res+=n%2
            n=n>>1
            
        return res
    
    def allOnes(self,n):
        dp=[0]*(n+1)
        offset=1
        for i in range(1,n+1):
            
            if offset*2==i:
                offset=i
            dp[i]=1+dp[i-offset]
            
        return offset
                
