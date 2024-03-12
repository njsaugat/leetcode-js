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
        if not root:
            return []

        
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
                
            temp.append(res)
        
        return res
    
    def  buildTree(self,preorder,inorder):
        
        if not preorder or not inorder:
            return None
        
        root=TreeNode(preorder[0])
        mid=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1])
        return root
    
    def kthSmallestBST(self,root,k):
        if not root:
            return None
        
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
            
        
    def lowestAncestor(self,root,p,q):
        
        while True:
            if root.val<p.val and root.val<q.val:
                root=root.left
            elif root.val>p.val and root.val>q.val:
                root=root.right
            else:
                return root
            
    def validBST(self,root):
        
        def isValid(leftVal,node,rightVal):
            if not node:
                return True
            if not(leftVal<node.val<rightVal):
                return False
            return isValid(leftVal,node.left,node.val) and isValid(node.val,node.right,rightVal)
        
        return isValid(float("-inf"),root,float("inf"))


    def isDuplicate(self,nums):
        numset=set()

        for num in nums:
            
            if num in numset:
                return True
            numset.add(num)
        return False
    
    def isAnagram(self,word1,word2):
        
        charset1={}
        charset2={}
        for char in word1:
            charset1[char]=1+charset1.get(char,0)
        
        for char in word2:
            charset2[char]=1+charset2.get(char,0)

        return charset2==charset1
    
    def topKElements(self,nums,k):
        freq_table=[[] for i in range(len(nums+1))]
        numset={}

        res=[]

        for num in nums:
            numset[num]=1+numset.get(num,0)
        
        for num,count in numset.items():
            freq_table[count].append(num)
        
        for i in range(len(freq_table)-1,0,-1):
            for num in freq_table[i]:
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

    def productExceptSelf(self,nums):
        
        output=[1]*len(nums)

        for i in range(1,len(nums)):
            output[i]=output[i-1]*nums[i-1]
        postfix=1
        
        for i in range(len(nums),-1,-1):
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

        
        
    def twoSum(self,nums,target):
        
        numset={}
        for i,num in enumerate(nums):
            
            diff=target-num
            if diff in numset:
                return [numset[diff],i]
            numset[num]=i
            
        return [-1,-1]

        
    def reverseLL(self,head):
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
    
    def mergeList(self,list1,list2):
        
        temp=curr=ListNode()

        while list1 and list2:
            
            if list1.val<list2.val:
                temp.next=list1
                list1=list1.next
                
            else:
                temp.next=list2
                list2=list2.next
                
            temp=temp.next

        temp.next=list1 or list2
        
        return curr.next
    
    def deleteNode(self,head,n):

        length=0
        curr=temp=head
        
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
    
    def isPalindrome(self,s):
        
        left,right=0,len(s)-1
        s=s.lower()
        while left<right:
            
            while not(s[left].isalpha() or s[left].isdigit()) and left<right:
                left+=1
            while not(s[right].isalpha() or s[right].isdigit()) and left<right:
                right-=1
                
            
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
            
            
        return True
    
    def mostContainer(self,height):
        
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
    
    def bestStocks(self,price):
        
        left,right=0,0
        max_profit=0
        while right<len(price):
            
            profit=price[right]-price[left]
            max_profit=max(max_profit,profit)

            if price[left]<price[right]:
                right+=1
            else:
                left=right
                right+=1
        return max_profit
    
    