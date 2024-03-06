class TreeNode:
    def __init__(self,left=None,val=0,right=None):
        self.left=left
        self.val=0
        self.right=right
class Solution:
    def buildTree(self,preorder,inorder):
        
        if not preorder or not inorder:
            return None
    
        root=TreeNode(val=preorder[0])
        mid=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])

        return root
        


class Solution:
    def buildTree(self,preorder,inorder):
        
        if not preorder or not inorder:
            return None

        root=TreeNode(preorder[0])
        mid=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])

        return root
    
    def buildTree(self,preorder,inorder):
        
        if not preorder or not inorder:
            return None
        
        root=TreeNode(preorder[0])
        mid=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])

        return root        







