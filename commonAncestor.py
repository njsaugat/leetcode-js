class Solution:
    def commonAncestor(self,root,p,q):
        
        while True:
            if root.val<p.val and root.val<q.val:
                root=root.right
            elif root.val>p.val and root.val>q.val:
                root=root.left
            else:
                return root
    
    
    def isValidBST(self,root):
        
        def isValid(node,leftVal,rightVal):
            
            if not node:
                return True
            if not(leftVal<node.val<rightVal):
                return False
            
            return isValid(node.left,leftVal,node.val) and isValid(node.right,node.val,rightVal)
            
            
        return isValid(root,float("-inf"),float("inf"))            


