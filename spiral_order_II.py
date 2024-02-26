class Solution:
    def spiral_order_two(self,n):
        matrix=[[1 for _ in range(n)] for _ in range(n)]
        curr=1
        top,bottom=0,n
        left,right=0,n
        
        while left<right and top<bottom:
            
            for i in range(left,right):
                matrix[top][i]=curr
                curr+=1

            top+=1
            
            for i in range(top,bottom):
                matrix[i][right-1]=curr
                curr+=1
                
            right-=1
            for i in range(right-1,left-1,-1):
                matrix[bottom-1][i]=curr
                curr+=1
            
            bottom-=1
            
            for i in range(bottom-1,top-1,-1):
                matrix[i][left]=curr
                curr+=1

            
            left+=1
        # for i in range(0,n):
        #     matrix[0].append(i+1)
        
        # for i in range(n):
        #     matrix[1]
        return matrix

print(Solution().spiral_order_two(3))