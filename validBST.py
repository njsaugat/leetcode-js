class Solution:
    def validBST(self,root):
        
        def isValid(node,leftVal,rightVal):
            if not node:
                return True
            if not (leftVal<node.val<rightVal):
                return False
            
            return isValid(node.left,leftVal,node.val) and isValid(node.right,node.val,rightVal)
        
        return isValid(root,float("-inf"),float("inf"))
    

    def validBST(self,root):
        def isValid(node,leftVal,rightVal):
            if not node:
                return True
            if not(leftVal<node.val<rightVal):
                return False
            
            return isValid(node.left,leftVal,node.val) and isValid(node.right,node.val,rightVal)
        
        return isValid(root,float("-infinity"),float("infinity"))
    
