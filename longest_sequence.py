class Solution:
    def consecutive_sequence(self,nums):
        
        nums.sort()
        res=curr=1
        for i in range(1,len(nums)):
            
            if nums[i]==nums[i-1]:
                continue
            if nums[i]-1==nums[i-1]:
                curr+=1
                res=max(curr,res)
            
            else:
                curr=1
        
        return res
    

# print(Solution().consecutive_sequence([]))

print(set([100,1,2,2,3,4,1]))