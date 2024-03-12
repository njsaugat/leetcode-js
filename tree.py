import collections 

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=None

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def invert(self,root):
        
        if not root:
            return None
        temp=root.left
        root.left=root.right
        root.right=temp
        
        self.invert(root.left)
        self.invert(root.right)
        
        return root
    
    def maxDepth(self,root):
        if not root:
            return 0
        
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
    
    def maxDepthS(self,root):
        
        if not root:
            return 0
        
        stack=[[root,1]]
        levels=0
        while stack:
            node,depth=stack.pop()

            if node:
                levels=max(depth,levels)

                stack.append([node.left,1+depth])
                stack.append([node.right,1+depth])

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
            return False
        if not tree:
            return False
        
        if self.isSameTree(tree,subTree):
            return True
        
        return self.isSubTree(tree.left,subTree) or self.isSubTree(tree.right,subTree)

    
    def buildTree(self,preorder,inorder):
        
        if not preorder or not inorder:
            return None
        
        root=TreeNode(preorder[0])        
        mid=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])

        return root
    
    def levelsOrder(self,root):
        
        if not root:
            return None
        
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
    
    
    def kthSmallest(self,root,k):

        stack=[]
        curr=root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr=curr.right
            
            curr=stack.pop()

            k-=1
            if k==0:
                return curr.val
            
            curr=curr.right
            
    def validBst(self,root):

        def isValid(leftVal,node,rightVal):
            
            if not node:
                return True
            
            if not(leftVal<node.val<rightVal):
                return False
            
            return isValid(leftVal,node.left,node.val) and isValid(node.val,node.right,rightVal)

        return isValid(float("-inf"),root,float("inft"))

        
    def lowestCommonAncestor(self,root,p,q):
        
        while True:
            if root.val<p.val and root.val<q.val:
                root=root.right
                
            elif root.val>p.val and root.val>q.val:
                root=root.left
            else:
                return root
            
    def hasDuplicate(self,nums):
        numset=set()
        for num in nums:
            if num in numset:
                return True
            
            numset.add(num)
        return False
    
    def isAnagram(self,word1,word2):
        
        charset1={}
        charset2={}

        for char in charset1:
            charset1[char]=1+charset1.get(char,0)

        for char in charset2:
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
    
    def topKElements(self,nums):
        
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
                
    def productExceptSelf(self,nums):
        output=[1]*len(nums)
        for i in range(1,len(nums)):
            output[i]=output[i-1]*nums[i-1]
        
        postfix=1
        for i in range(len(output)-1,-1,-1):
            
            output[i]=output[i]*postfix
            postfix=postfix*nums[i]
        
        return output
    
    def isValidAnagram(self,words):
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
        longest=0
        numset=set(nums)
        for num in numset:
            if num-1 not in numset:
                length=1
                while num+length in numset:
                    length+=1
                
                longest=max(longest,length)
        
        return longest            
    
    def isValidSudoku(self,board):
        
        rows=collections.defaultdict(set )
        cols=collections.defaultdict(set )
        squares=collections.defaultdict(set )
        for r in range(9):
            for c in range(9):
                
                if board[r][c]==".":
                    continue
                
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[r//3,c//3] 
                ):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[r//3,c//3].add(board[r][c])
                
        return True
    
    
    
    def reverseLL(self,head):
        p=None
        q=head
        r=r.next
        
        while q:
            q.next=p
            p=q
            q=r
            if r:
                r=r.next
        return p
    
    def hasCycle(self,head):
        slow=fast=head
        
        while fast and fast.next:
            
            slow=slow.next
            fast=fast.next.next
            
            if slow==fast:
                return True
            
        return False
    
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
    
    def removeList(self,head,n):
        
        if not head:
            return None
        
        temp=curr=head
        length=1
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
    
    
    def isPalindrome(self,str):
        
        left,right=0,len(str)-1
        str=str.lower()
        while left<right:
            
            while not(str[left].isalpha() or str[left].isdigit()) and left<right:
                left+=1
            while not(str[right].isalpha() or str[right].isdigit()) and left<right:
                right-=1
                
            
            if str[left]!=str[right]:
                return False
            
            left+=1
            right-=1
            
        return True
    
    def mostWater(self,height):
        
        left,right=0,len(height)
        res=0
        while left<right:
            
            area=min(height[left],height[right])*(right-left)
            res=max(res,area)
            
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
                
        return res
    
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
    
    def maxStocks(self,prices):
        
        left,right=0,0
        max_profit=0
        while right<len(prices):
            profit=prices[right]-prices[left]
            max_profit=max(profit,max_profit)

            if prices[left]<prices[right]:
                right+=1
                
            else:
                left=right
                righ+=1
                
        return max_profit
    
    def longestSubstring(self,str):
        charset={}
        longest=1
        left,right=0,0
        
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
    
    
    
    def search(self,nums,target):
        left,right=0,len(nums)-1
        
        while left<=right:

            mid=left+(right-left)//2
            
            if nums[mid]==target:
                return mid
            elif nums[left]<=nums[mid]:
                if target>nums[mid] or target<nums[left]:
                    left+=1
                else:
                    right-=1
            else:
                if target<nums[mid] or target>nums[right]:
                    right-=1
                else:
                    left+=1
                    
        return -1
    
    def minSorted(self,nums):
        
        curr_min =float("inf")
        left,right=0,len(nums)-1
        
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

    
    def spiral(self,matrix):
        
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
    
    
    def climbStairs(self,n):
        if n<=3:
            return n
        n1,n2=2,3
        
        for i in range(4,n+1):
            temp=n1+n2
            n1=n2
            n2=temp
        return n2
    
    def rob(self,nums):
        
        rob1,rob2=0,0
        
        for num in nums:
            temp=max(rob1+num,rob2)
            rob1=rob2
            rob2=temp
            
        return rob2
    
    def maxRob(self,nums):
        return max(nums[0],self.rob(nums[1:]),self.rob(nums[:-1]))
    
    def countPalindrome(self,s,l,r):
        res=0
        while l>=0 and r<len(s) and s[l]==s[r]:
            res+=1
            l-=1
            r+=1
            
        return res
    
    def palindrome(self,s):
        res=0
        
        for i in range(len(s)):
            res+=self.countPalindrome(s,i,i)
            res+=self.countPalindrome(s,i,i+1)
        
        return res
    
    def wordBreak(self,s,wordDict):
        dp=[False]*(len(s)+1)
        dp[len(s)]=True
        
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i+len(w)<=len(s) and s[i:i+len(w)]==w):
                    dp[i]=dp[i+len(w)]
                if dp[i]:
                    break
                
        return dp[0]