class Solution:
    
    def sortColors(self,nums):

        i,j=0,len(nums)-1
        
        while i<j:
            # [0,0,1,1,0,1,1,1,1]
            # [1,0,1,1,0,1,0,1,0] 
            # [0,0,1,1,0,1,0,1,1] 
            # [0,0,1,1,0,1,0,1,0]
            if nums[i]==1 :
                i+=1
            if nums[j]==1:
                j-=1
            if nums[i]==2 and nums[j]==0:
                nums[i],nums[j]=0,2
                i+=1
                j-=1
            
            elif nums[i]==0 and nums[j]==2:
                i+=1
                j-=1
            elif nums[i]==0 and nums[j]==0:
                i+=1
            elif nums[i]==2 and nums[j]==2:
                j-=1
        
        
        return nums



    
    def sortColors2(self,nums):
        count0=0
        count1=0
        count2=0
        for num in nums:
            if num ==0:
                count0+=1
            elif num ==1:
                count1+=1
            else:
                count2+=1
                
        # numsDup=[0]*len(nums)
        nums[0:count0]=[0]*count0
        nums[count0:count0+count1]=[1]*count1
        nums[count0+count1:len(nums)]=[2]*count2
        return nums
    def sortColors3(self,nums):
        
        i,j=0,len(nums)-1
        
        while i<j:
            '''
            
            012
            021
            102
            120
            210
            201
                        
            '''
            # if 
    
    
    def sortColorsAll(self,nums):
        
        left,mid,right=0,0,len(nums)-1
        
        while mid<=right:
            if nums[mid]==0:
                nums[left],nums[mid]=nums[mid],nums[left]
                left+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[right]=nums[right],nums[mid]
                right-=1
                

print(Solution().sortColors2([2,0,1] ))            