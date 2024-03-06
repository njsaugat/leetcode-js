import collections
class TreeNode:
    def __init__(self,left=None,val=0,right=None):
        self.left=left
        self.val=val
        self.right=right
        
  
  
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=None      
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

        
    def levelsOrder(self,root):
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
            res.append(temp)
        
        return res
    
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
    
    
    def lowestCommonAncestor(self,root,p,q):
        while True:
            if root.val<p.val and root.val<q.val:
                root=root.right
                
            elif root.val>p.val and root.val>q.val:
                root=root.left
                
            else:
                return root
            
            
    def kthSmallestElement(self,root,k):
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
            
    
    def validateBST(self,root):
        
        def valid(leftVal,node,rightVal):
            
            if not node:
                return True
            
            if not(leftVal<node.val<rightVal):
                return False
            
            return valid(leftVal,node.left,node.val) and valid(node.val,node.right,rightVal)
    
        
        return valid(float("-inf"),root,float("inf"))    


    def buildTree(self,preorder,inorder):
        
        if not (preorder and inorder):
            return None
        
        root=TreeNode(None,preorder[0],None)
        mid=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])
        
        return root
    
    
    
class SolutionLinkedList:
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
    
    def hasCycle(self,head):
        slow=fast=head
        
        while fast and fast.next:
            
            slow=slow.next
            fast=fast.next.next
            
            if slow==fast:
                return True
            
        return False
    
    def removeFromList(self,head,n):

        if not head:
            return None
        
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
    
    
    

class SolutionArray:
    def hasDuplicate(self,nums):
        numset=set()
        
        for num in nums:
            if num in numset:
                return True
            numset.add(num)
        
        return False
    
    def twoSum(self,nums,target):
        numset={}
        for i,num in enumerate(nums):
            
            diff=target-num
            if diff in numset:
                return [numset[diff],i]
            
            numset[num]=i
            
        return [-1,-1]
    
    def validAnagram(self,word1,word2):
        
        charset1={}
        charset2={}

        for char in word1:
            charset1[char]=1+charset1.get(char,0)

        for char in word2:
            charset2[char]=1+charset2.get(char,0)
        
        return charset1==charset2
    
    def groupAnagrams(self,words):
        output={}
        for word in words:
            letters=[0]*26
            
            for char in word:
                
                diff =ord(char)-ord("a")
                letters[diff]+=1
            key=repr(letters)
            output[key]=output.get(key,[])
            output[key].append(word)
        
        
        return [value for key,value in output.items()]

        
    
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
                if len(res)==0:
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
            
            if (num-1) not in numset:
                length=1
                while (num+length) in numset:
                    length+=1
                longest=max(longest,length)
            
        return longest
    
    

class Solution2Pointer:
    def isPalindrome(self,str):
        
        if len(str)==0:
            return True
        
        left,right=0,len(str)-1
        
        while left<right:
            
            while not (str[left].isalpha() or str[left].isdigit()) and left<right:
                left+=1
            while not (str[right].isalpha() or str[right].isdigit()) and left<right:
                right-=1
            
            if str[left].lower()!=str[right].lower():
                return False
            left+=1
            right-=1
            

        return True

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
    

class SolutionSliding:
    def bestStock(self,prices):
        
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
    
    def longestSequence(self,str):
        
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
            longest=max(len(charset),longest)
            right+=1
            
        return longest
            


class SolutionBinary:
    def search(self,nums,target):
        
        left,right=0,len(nums)-1
        
        while left<=right:
            
            mid=left+(right-left)//2
            
            if nums[mid]==target:
                return mid
            if nums[left]<=nums[right]:
                
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
    
    
    def minSorted(self,nums):
        
        left,right=0,len(nums)-1
        curr_min=float("inf")
        while left<right:
            
            mid=left+(right-left)//2
            
            curr_min=min(nums[mid],curr_min)
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
        
                
            

                
            