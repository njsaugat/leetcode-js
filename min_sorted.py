class Solution:
    def min_sorted(self,nums):
        
        left,right=0,len(nums)-1
        curr_min=float("infinity")
        if nums[left]<nums[right]:
            return nums[0]
        while left<right:
            
            mid=left+(right-left)//2
            curr_min=min(curr_min,nums[mid])

            if nums[mid]>nums[left]: #5,1,2,3,4
                left=mid+1
            else:
                right=mid-1
    
        return min(curr_min,nums[left])
        # return 

print(Solution().min_sorted([4,5,1,2,3]))

        