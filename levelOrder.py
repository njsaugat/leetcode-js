import collections
class Solution:
    def levelOrder(self,root):
        q=collections.deque([root])
        res=[]
        while q:
            temp=[]
            for i in range(len(q)):
                node=q.popleft()

                temp.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            res.append(temp)
            
        return res