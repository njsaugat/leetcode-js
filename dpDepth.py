class Solution:
    def stairwayToHeaven(self,n):
        finalStep=n
        def helper(num):

            if num>finalStep:
                return 0
            if num==finalStep:
                return 1
            
            return helper(num+1) + helper(num+2)            
            
            
        return helper(0)
    
    def robHouse(self,nums):
        n=len(nums)
        def helper(nums):
            
            # recurrence relation
            return max(helper(nums[0:]+nums[2:n]),helper(nums[1:n]))
            
            
            
print(Solution().stairwayToHeaven(10))