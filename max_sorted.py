class Solution:
    def max_sorted(self,nums):
        
        left,right=0,len(nums)-1
        curr_max=float("-infinity")
        while left<right:
            
            mid=left+(right-left)//2
            curr_max=max(curr_max,nums[mid])
            if nums[mid]<nums[right]:
                left=mid+1
            elif nums[mid]<=nums[left]:
                right=mid-1
            elif nums[mid]>nums[left]:
                left=mid+1
            elif nums[mid]>=nums[right]:
                right=mid-1
                
        return max(curr_max,nums[right])
    
print(Solution().max_sorted([1,2,3,4,5]))