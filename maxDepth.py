import collections
class Solution:
    def maxDepth(self,root):
        
        if not root:
            return 0
        
        
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
    
    
    def maxDepthQ(self,root):
        if not root:
            return 0
        
        q=collections.deque([root])
        levels=0
        while q:
            
            for i in range(len(q)):
                
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
            
            levels+=1
        
        return levels
                
                
    def maxDepthStack(self,root):
        if not root:
            return 0
        
        levels=0
        
        stack=[[root,1]]
        while stack:
            node,depth=stack.pop()

            if node:
                levels=max(levels,depth)
                stack.append([node.left,1+depth])
                stack.append([node.right,1+depth])
            
            
        return levels