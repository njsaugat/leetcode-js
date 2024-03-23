import collections


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
        
        

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
        
        

class Solution:
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
            charset1[char]=1+charset1.get(char,0)
        for char in word2:
            charset2[char]=1+charset2.get(char,0)
        
        return charset1==charset2
    
    
    def twoSum(self,nums,target):
        numset={}
        for i,num in enumerate(nums):
            
            diff=target-num

            if diff in numset:
                return [numset[diff],i]

            numset[num]=i
        
        return [-1,-1]
    
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

    
    def topKElements(self,nums,k):
        
        frequencey_table=[[]for i in range(len(nums)+1)]

        numset={}
        res=[]

        for num in nums:
            numset[num]=1+numset.get(num,0)
        
        for num,count in numset.items():
            frequencey_table[count].append(num)

        
        for i in range(len(frequencey_table)-1.0,-1):
            for num in range(frequencey_table[i]):
                res.append(num)
                if len(res)==k:
                    return res
                
                
    def productExceptSelf(self,nums):
        
        output=[1]*len(nums)

        for i in range(1,len(nums)):
            output[i]=output[i-1]*nums[i-1]
        
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            output[i]=output[i]*postfix
            postfix=postfix*nums[i]    
        
        return output
    
    def longestSequence(self,nums):
        
        numset=set(nums)
        longest=0
        for num in numset:
            
            if num-1 not in numset:
                length=1
                while num+length in numset:
                    length+=1

                longest=max(longest,length)
            
            
        return longest
    
    
    def isSudoku(self,board):
        
        rows=collections.defaultdict(set)
        cols=collections.defaultdict(set)
        squares=collections.defaultdict(set)

        
        for row in range(9):
            for col in range(9):
                
                if (board[row][col]=="."):
                    continue
                
                if (
                    board[row][col] in rows[row]
                    or board[row][col] in cols[col]
                    or board[row][col] in squares[row//3,cols//3]
                ):
                    return False
                
                
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[row//3,col//3].add(board[row][col])
            
        return True
    
    
        
    
    def isPalindrome(self,s):
        left,right=0,len(s)-1
        s=s.lower()
        while left<right:
            
            while not(s[left].isalpha()or s[left].isdigit()) and left<right:
                left+=1
            while not(s[right].isalpha()or s[right].isdigit()) and left<right:
                right-=1
            
            
            if s[left]!=s[right]:
                return False
            
            left+=1
            right-=1
            
        return True
        
    
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
    
    
    def mostWaters(self,heights):
        
        
        left,right=0,len(heights)-1
        res=0
        while left<right:
            area=min(heights[left],heights[right])*(right-left)
            res=max(area,res)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
                
        return res
    
    
    def maxStocks(self,prices):
        left,right=0,0
        
        while right<len(prices):
            profit=prices[right]-prices[left]
            maxProfit=max(profit,maxProfit)
            
            if prices[left]<prices[right]:
                right+=1
            else:
                left=right
                right+=1
                
        return maxProfit
    
    
    def longestNonRepeating(self,s):
        
        charset={}

        left,right=0,0
        longest=0
        while right<len(s):
            
            if s[right] in charset:
                left=1+charset[s[right]]
                charset={}
                
                while left<right:
                    charset[s[left]]=left
                    left+=1
            
            charset[s[right]]=right
            longest=max(longest,len(charset))
            right+=1
            
        return longest
    
    def search(self,nums,target):
        
        left,right=0,len(nums)-1
        
        while left<=right:
            
            mid=left+(right-left)//2
            
            if nums[mid]==target:
                return mid
            elif nums[left]<=nums[mid]:
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
    
    
    def findMinSorted(self,nums):
        
        left,right=0,len(nums)-1
        currMin=float("inf")
        while left<right:
            mid=left+(right-left)//2
            currMin=min(currMin,nums[mid])
            
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
        
        return min(currMin,nums[left])

    
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
    
    def removeFromList(self,head,n):
        
        temp=curr=head
        length=0
        while temp:
            length+=1
            temp=temp.next
            
        position=length-n
        if position==0:
            return head.next
        
        
        for i in range(1,position):
            curr=curr.next
        
        deleteNode=curr.next
        
        curr.next=deleteNode.next
        
        return head
    
    def hasCycle(self,head):
        slow=fast=head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
            if slow==fast:
                return True
            
        return False
    
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
    
    def maxDepthS(self,root):
        
        if not root:
            return 0
        
        depths=0
        
        stack=[[root,1]]

        while stack:
            
            node,depth=stack.pop()

            if node:
                depths=max(depth,depths)

                stack.append([node.left,1+depth])
                stack.append([node.right,1+depth])
        
        return depths
    
    
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
    
    
    def levelsOrder(self,root):
        
        res=[]

        q=collections.deque([root])

        while q:
            temp=[]
            for i in range(len(q)):
                
                node=q.popleft()
                temp.append(node.val)
                if node.right:
                    q.append(node.right)
                if node.right:
                    q.append(node.right)
                
            res.append(temp)

        return res
    
    def lowestAncestor(self,root,p,q):
        while True:
            if root.val<p.val and root.val<q.val:
                root=root.right
                
            elif root.val>p.val and root.val>q.val:
                root=root.left
            else:
                return root
    def isValidBST(self,root):
        
        def isValid(leftVal,node,rightVal):
            
            if not node:
                return True
            
            if not(leftVal<node.val<rightVal):
                return False
            
            return isValid(leftVal,node.left,node.val) and isValid(node.val,node.right,rightVal)            
        
        return isValid(float("-inf"),root,float("inf"))
    
    
    def kthSmallest(self,root,k):
        
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
        
    def buildTree(self,preorder,inorder):
        
        if not preorder or not inorder:
            return None
        
        root=TreeNode(preorder[0])
        mid=inorder.index(preorder[0])

        root.left=self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1])
        return root
    
    
    
    def mergeIntervals(self,intervals):
        intervals.sort(key=lambda i:i[0])

        output=[intervals[0]]

        for i in range(1,len(intervals)):
            j=len(output)-1
            start,end=0,1
            currInterval,prevInterval=intervals[i],output[j]

            if currInterval[start]<=prevInterval[end]:
                maxEnd=max(currInterval[end],prevInterval[end])
                output[j]=[prevInterval[start],maxEnd]
            else:
                output.append(intervals[i])
        
        return intervals
    
    
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
            
            if not(top<bottom and left<right):
                break
            
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            
            bottom-=1
            
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            
            return res
        
        
    def hammingWeight(self,n):
        
        res=0
        while n:
            res+=n%2
            n=n>>1
        
        return res
    
    def countingBits(self,n):
        dp=[0]*(n+1)
        offset=1
        for i in range(1,n+1):
            
            if offset*2==i:
                offset=i
            dp[i]=1+dp[i-offset]

        return dp
    
    def missingNum(self,nums):
        missing=0
        for i in range(len(nums)):
            missing+=(i-nums[i])
        return missing
    


    def climbStairs(self,n):
        
        num1,num2=0,1
        
        for i in range(n):
            temp=num1+num2
            num1=num2
            num2=temp
            
        return num2
    
    
    def rob(self,nums):
        rob1,rob2=0,0
        for num in nums:
            newRob=max(rob1+num,rob2)
            rob1=rob2
            rob2=newRob
        
        return rob2
    
    def robII(self,nums):
        if len(nums)==1:
            return nums[0]
        
        return max(self.rob(nums[1:]),self.rob(nums[:-1]))


    def countPalindrome(self,s,l,r):
        res=0
        
        while l>=0 and r<len(s) and s[l]==s[r]:
            res+=1
            l-=1
            r+=1
        
        return res
    
    def totalPalindromes(self,s):
        res=0
        
        for i in range(len(s)):
            
            res+=self.countPalindrome(s,i,i)
            res+=self.countPalindrome(s,i,i+1)
        
        return res
    
    
    def findLongestSubtring(self,s):
        res=''
        resLen=0
            
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if len(res)<(r-l+1):
                    res=s[l:r+1]
                    resLen=r-l+1
                
                l-=1
                r+=1 
            l,r=i,i+1 
            
            while l>=0 and r<len(s) and s[l]==s[r]:
                if len(res)<(r-l+1):
                    res=s[l:r+1]
                    resLen=r-l+1
                
                l-=1
                r+=1   
        return res
    
