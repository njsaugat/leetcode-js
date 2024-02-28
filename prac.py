class Solution:
    def threeSum(self,nums):
        nums.sort()
        res=[]

        for i,num in enumerate(nums):
        
            if i>0 and nums[i-1]==num:
                continue

            left,right=1,len(nums)-1
            
            while left<right:
                
                threeSum=num+nums[left]+nums[right]
                
                if threeSum<0:
                    left+=1
                elif threeSum>0:
                    right-=1
                else:
                    res.append([num,nums[left],nums[right]])
                    left+=1
                    while nums[left-1]==nums[left] and left<right:
                        left+=1
        
        return res
    
    def twoSum(self,nums,target):
        hashset={}

        for i,num in nums:
            diff=target-num
            if diff in hashset:
                return [hashset[diff],i]
            
            hashset[num]=i
            
        return [-1,-1]
    
    
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

    
    def hammingWeight(self,num):
        res=0
        while num:
            res+=num%2
            num=num>>1
            
        return res
    
    def total_ones(self,n):
        dp=[0]* (n+1)
        offset=1
        for i in range(1,n+1):
            
            if offset*2==i:
                offset=i
            dp[i]=1+dp[i-offset]
            
        return dp
    
    def missing(self,nums):
        n=len(nums)
        missing=(n*(n+1))//2
        
        for num in nums:
            missing-=num
        
        return missing
    
    def stock_buy(self,prices):
        
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
    
    
    def has_duplicate(self,nums):
        numset=set()

        for num in nums:
            
            if num in numset:
                return True
            
            numset.add(num)
            
        return False
    
    def valid_anagram(self,word1,word2):
        
        charSet1={}
        charSet2={}

        for char in word1:
            charSet1[char]=1+charSet1.get(char,0) 
        for char in word2:
            charSet2[char]=1+charSet2.get(char,0) 
        
        return charSet1==charSet2
    
    
    def topKElements(self,nums,k):
        
        freq_table=[[] for i in range(len(nums)+1)]
        
        res=[]
        numset={}
        for num in nums:
            numset[num]=1+numset.get(num,0)
        
        for num,count in numset.items():
            freq_table[count].append(num)

        for i in range(len(freq_table)-1,0,-1):
            for num in freq_table[i]:
                res.append(num)
                if len(res)==k:
                    return res
        
        
    
    def longest_sequence(self,nums):
        
        longest=0
        numset=set(nums)
        for num in nums:
            
            if (num-1) not in nums:
                
                length=1

                while (num+length) in numset:
                    length+=1
                    
                longest=max(longest,length)
        
        return longest
    
    
    
    def valid_palindrome(self,str):
        if len(str)==0:
            return False
        if len(str)==1:
            return True
        
        left,right=0,len(str)-1
        
        while left<right:
            
            while not(str[left].isalpha() or  str[left].isdigit()) and left<right:
                left+=1
            while not(str[right].isalpha() or  str[right].isdigit()) and left<right:
                right-=1
            
            if str[left]!=str[right]:
                return False
            
        
        return True

    

    def longest_sequence(self,str):
        
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
    
        return longest


    def minimum_sorted(self,nums):
        
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
                # 5,1,2,3,4
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

            elif nums[left]<=nums[mid]:
                # 4,5,6,7,0,1,2
                if target>nums[mid] or target<nums[left] :
                    left=mid+1
                else:
                    right=mid-1
        
            else:
                if target<nums[mid] or target>nums[right]:
                    right=mid-1
                else:
                    left=mid+1
        return -1
        
        
    
    def rotate_image(self,matrix):
        
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
                
        
        for i in range(len(matrix)):
            matrix[i]=matrix[i][::-1]
            

        return matrix

    
    def spiral_matrix(self,matrix):
        
        res=[]
        top,bottom=0,len(matrix)
        left,right=0,len(matrix[0])
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
    
    
    def has_cycle(self,head):
        slow=fast=head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
            if slow==fast:
                return True
            
            
        return False
    
    def reverse_list(self,head):
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
    
    def merge_intervals(self,intervals):
        intervals.sort(key=lambda i:i[0])

        output=[intervals[0]]
        j=0
        for i in range(1,len(intervals)):
            
            curr_interval,prev_interval=intervals[i],output[j]
            start,end=0,0
            
            if curr_interval[start]<=prev_interval[end]:
                max_end=max(curr_interval[end],prev_interval[end])
                output[j]=[prev_interval[start],max_end]
            else:
                output.append(intervals[i])
                j+=1
                
        return output
    
    def longest_repeating_character(self,str,k):
        charset={}
        print(enumerate(str))
        for i,char in enumerate(str):
            # charset[char]=1+charset.get(char,0)
            charset[char]=i

        return charset
    

    def merge_linked_lists(self,list1, list2):
        if not(list1) and list2:
            return list2
        if not(list2) and list1:
            return list1

        temp=ListNode() #
        head=None
        while list1 and list2:
            newnode=ListNode()
            if list1.val<list2.val:
                newnode.val=list1.val
                temp.next=newnode
                temp=newnode
                list1=list1.next
            
            else:
                newnode.val=list2.val
                temp.next=newnode
                temp=newnode
                list2=list2.next
                
            if not(head):
                head=temp
        
        while list1:
            newnode=ListNode()
            newnode.val=list1.val
            temp.next=newnode
            temp=newnode
            list1=list1.next
        
        while list2:
            newnode=ListNode()
            newnode.val=list2.val
            temp.next=newnode
            temp=newnode
            list2=list2.next
        
        return head 
                # temp.next=




    def merge_lists_fast(self,list1,list2):
        if not(list1) and list2:
            return list2
        if not(list2) and list1:
            return list1
        p,q=None,None
        r,s=list1,list2
        head=None
        while r and s:     
            if r.val<=s.val:
                p=r
                if q:
                    q.next=p
                r=r.next
            
            else:
                q=s
                if p:
                    p.next=q
                s=s.next
            
            
            if not head:
                head=p or q
            
        
        if r:
            q.next=r
        if s:
            p.next=s 
            
        return head
    
    def matrix_search(self,matrix,target):
        
        left,right=0,len(matrix[0])-1
        top,bottom=0,len(matrix)-1
        total_length=(right+1)*(bottom+1)
        """
        1 2 3
        4 5 6
        7 8 9
        1   2  3  4  5
        6   7  8  9  10 
        11 12 13  14 15
        16 17 18  19 20
        21 22 23  24 25 
        """
        while left<=right and top<=bottom:
            mid_row=top+(bottom-top)//2
            mid_col=left+(right-left)//2
            
            if matrix[mid_row][mid_col]==target:
                return True
            
            elif matrix[mid_row][mid_col]<target:
                # apt matrix
                if matrix[mid_row][left]<=target<=matrix[mid_row][right]:
                    right=mid_col-1
                else:
                    bottom=mid_row-1                    
                    
                
            else:
                if matrix[mid_row][left]<=target<=matrix[mid_row][right]:
                    left=mid_col+1
                else:
                    top=mid_row+1
                    
            
        return False

    
    
                    
            
class ListNode:
    head=None
    def __init__(self,val=0,next=None) :
        self.val=val
        self.next=next
    
    # def insert(self,val):
        # if head:

# last1=ListNode(7,None)      
last1=ListNode(4,None)      
middle1=ListNode(2,last1)
head1=ListNode(1,middle1)

last2=ListNode(4,None)      
middle2=ListNode(3,last2)
head2=ListNode(1,middle2)



head=Solution().merge_lists_fast(head1,head2)
temp=head
while(temp):
    print(temp.val)
    temp=temp.next




# print(Solution().merge_linked_lists(head1,head2))
            
# print(Solution().longest_repeating_character("ABAABBA",2))
                
                
