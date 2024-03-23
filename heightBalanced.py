import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Tree:
    def createTree(self,nums):

        root=TreeNode(nums[0])
        q=collections.deque([root])        
        i=0
        length=len(q)
        while(i+length+1<len(nums)):
            length=len(q)
            node=q.popleft()
            if nums[i+length] and node:
                node.left=TreeNode(nums[i+length])
            if nums[i+length+1] and node:
                node.right=TreeNode(nums[i+length+1])
            if node:
                q.append(node.left)
                q.append(node.right)
            i+=1
        
        return root
                
                
class Solution:
    def isBalanced(self, root) :
        def helper(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            
            
            leftHeight=helper(root.left)
            rightHeight=helper(root.right)
            return leftHeight-rightHeight

        height=helper(root)

        if abs(height)>1:
            return False
        return True
    



root=Tree().createTree([1,None,2,None,3])
# print(root)

print(Solution().isBalanced(root))

