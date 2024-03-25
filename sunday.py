import collections

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right
        

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
    
    
    def isAnagram(self,word1,word2):
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
            letter=[0]*26

            for char in word:
                diff=ord(char)-ord("a")
                letter[diff]+=1
            
            key=repr(letter)
            output[key]=output.get(key,[])
            output.append(word)
        
        
        return [value for key,value in output.items()]
    
    
    def topKElements(self,nums,k):
        
        freq_table=[[] for i in range(len(nums)+1)]

        res=[]

        numset={}

        for num in nums:
            numset[num]=numset.get(num,0)
        
        for num,count in numset.items():
            freq_table[count].append(num)
        
        for i in range(len(freq_table)-1,-1,-1):
            for num in freq_table[i]:
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
    
    def validPalindrome(self,s):
        
        s=s.lower()
        left,right=0,len(s)-1
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
                    
    
    def threeSum(self,nums):
        res=[]
        nums.sort()
        for i,num in enumerate(nums):

            if i>0 and num ==nums[i-1]:
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
                    while left<right and nums[left] == nums[left-1]:
                        left+=1
                    
                    
        return res
    
    def mostContainer(self,height):
        
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
    
    
    def stocksBuy(self,prices):
        
        left,right=0,0
        maxProfit=0
        while right<len(prices):
            profit=prices[right]-prices[left]
            maxProfit=max(maxProfit,profit)

            if prices[left]<prices[right]:
                right+=1
            else:
                left=right
            
        
        return maxProfit
                
            
        
    def longestSubstring(self,s):
        
        left,right=0,0
        longest=0
        charset={}
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
    

    def mergeList(self,list1,list2):
        
        temp=head=ListNode()

        while list1 and list2:
            
            
            if list1.val<list2.val:
                temp.next=list1
                list1=list1.next
            
            else:
                temp.next=list2
                list2=list2.next
            
            temp=temp.next
            
    
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

        stack=[[root,0]]

        while stack:
            
            node,depth=stack.pop()

            if node:
                
                depths=max(depths,depth)

                node.append([root.left,1+depth])
                node.append([root.right,1+depth])
            
        return depths
    
    
    def isSameTree(self,p,q):
        
        if not q and not q:
            return True
        if not p or not q:
            return False
        if p.val !=q.val:
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
    
    
    def levelsOrderTraversal(self,root):
        
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
    
    
    def lowestAncestor(self,p,q,root):
        
        while True:
            
            if root.val<p.val and root.val<q.val:
                root=root.right
            elif root.val>p.val and root.val>q.val:
                root=root.left
                
            else:
                return root
            
        
    def validateBST(self,root):
        
        def isValid(leftVal,node,rightVal):
            
            if not node:
                return True
            if not(leftVal<node.val<rightVal):
                return False
            
            return isValid(leftVal,node.left,node.val) and isValid(node.val,node.right,rightVal)
        
        return isValid(float("-inf"),root,float("inf"))
    
    
    def kthSmallest(self,root):
        
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
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])
    
        return root
    
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
    
    
    
    def hammingWeight(self,n):
        res=0
        
        while n:
            res+=n%2
            n=n>>1
        
        return res
    
    def findMissingNum(self,nums):
        missing=0
        for i in range(len(nums)):
            missing+=(i-nums[i])
        
        return missing 

    def countingBits(self,n):
        
        
        dp=[0]*(n+1)
        offset=1
        for i in range(1,n+1):
            if offset*i==2:
                offset=i
            
            dp[i]=1+dp[i-offset]

        return dp
            
    
        
    def spiralMatrix(self,matrix):
        
        
        res=[]

        top,bottom=0,len(matrix)
        left,right=0,len(matrix[0])
        
        while top<bottom and left<right:
            
            for i in range(left,right):
                res.append(matrix[top][i])
        

            top+=1
            
            for i in range(top,bottom):
                res.append(matrix[right-1][i])
            
            right-=1
            
            if not(top<bottom and left<right):
                break
            
            
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            
            bottom-=1
            
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            
            
            left+=1
        
        return res
            
            
    def mergeIntervals(self,intervals):
        
        intervals.sort(key=lambda i:i[0] )

        output=[intervals[0]]

        for i in range(1,len(intervals)):
            j=len(output)
            currInterval,prevInterval=intervals[i],output[j]
            start,end=0,1
            if prevInterval[end]<=currInterval[start]:
                maxEnd=max(prevInterval[end],currInterval[end])
                output[j]=[prevInterval[start],maxEnd]
            else:
                output.append(currInterval)
            
        return output
    
    def rotateImage(self,matrix):
        
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
                
        
        for i in range(len(matrix)):
            matrix[i]=matrix[i][::-1]
        
        
        return matrix
    
    
    def climbStairs(self,n):
        
        n1,n2=0,1
        
        for i in range(1,n):
            
            temp=n1+n2
            n1=n2
            n2=temp
        
        return n2
    
    def rob(self,houses):
        
        rob1,rob2=0,0
        
        for house in houses:

            newRob=max(rob1+house,rob2)
            rob1=rob2
            rob2=newRob
            
        
        
        return rob2
    
    def houseRob(self,houses):
        
        return max(houses[0],self.rob(houses[1:]),self.rob(houses[:-1]))
    
    def totalPalindromes(self,s):
        res=0
        for i in range(len(s)):
            
            res+=self.countPalindromes(s,i,i)
            res+=self.countPalindromes(s,i,i+1)
        
        return res
            
    
    
    def countPalindromes(self,s,l,r):
        res=0
        while s[l]==s[r] and l>=0 and r<len(s):
            res+=1
            l-=1
            r+=1
        
        return res
    
    def longestPalindrome(self,s):
        res=''
        for i in range(len(s)):
            l,r=i,i        
            
            while s[l]==s[r] and l>=0 and r<len(s):
                if len(res)<(r-l+1):
                    res=s[l:r+1]
                l-=1
                r+=1    
            l,r=i,i+1
            while s[l]==s[r] and l>=0 and r<len(s):
                if len(res)<(r-l+1):
                    res=s[l:r+1]
                
                l-=1
                r+=1    
            
                    
        
    
    def decodeWaysR(self,s):
        dp={len(s):1}
        def helper(index):
            
            if index in dp:
                return dp[index]
            
            if s[index]=="0":
                return 0
            
            ways=helper(index+1)
            if index < len(s) - 1 and (s[index]=="1" or s[index]=="2" and s[index+1] in "0123456"):
                ways+=helper(index+2)
             
            dp[index]=ways           
            return ways
    

        return helper(0)
    
    
print(Solution().decodeWaysR("142"))

            
            


        
        