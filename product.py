class Solution:
    def productExceptSelf(self,nums):
        
        output=[1]*len(nums)
        
        for i in range(1,len(nums)):
            output[i]=output[i-1]*nums[i-1]
            
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            output[i]=output[i]*postfix
            postfix=postfix*nums[i]
            
        return output


    def validBST(self,root):
        
        def isValid(node,leftVal,rightVal):

            if not node:
                return True
            
            if not (leftVal<node.val<rightVal):
                return False
            
            return isValid(node.left,leftVal,node.val) and isValid(node.right,node.val,rightVal)

        
        
        return isValid(root,float("-inf"),float("inf"))    
print(Solution().productExceptSelf([1,2,3,4]))
