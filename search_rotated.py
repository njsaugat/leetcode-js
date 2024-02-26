class Solution:
    def search(self,nums,target):
        
        left,right=0,len(nums)-1
        
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                return mid

            elif nums[left]<nums[mid]:
                # [7,0,1,2,4,5,6]
                # 7>6 target>nums[mid] -->left=mid+1
                # 4<6 target<nums[mid] -->right=mid-1
                # 2<4 target<nums[left] -->left=mid+1
                # 4>7 4>5 4<4
                if target>nums[mid] or target<nums[left]:
                    left=mid+1
                else:
                    right=mid-1
                    
            else:
                if target<nums[mid] or target>nums[left]:
                    right=mid-1
                # elif target<=nums[left]:
                else:
                    left=mid+1
                # elif target>nums[right]:
                    # right=mid-1
    
        if nums[left]==target:
            return left
        return -1
    
print(Solution().search([4,5,6,7,0,1,2],4))                