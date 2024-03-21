class Solution:
    def printPositiveNums(self):
        res=[]
        for a in range(1000):
            for b in range(1000):
                for c in range(1000):
                    for d in range(1000):
                        sumLeft=pow(a,3)+pow(b,3)
                        sumRight=pow(c,3)+pow(d,3)

                        if sumLeft==sumRight:
                            res.append([a,b,c,d])
        
        return res
    
    
    
    
    
    def characterReplacement(self,s,k):
        
        if len(s)==0:
            return 0
        left,right=0,1
        length=1
        longest=0
        visited=[False]*len(s)
        while right<len(s):
            
            
            if s[right]==s[right-1] or (visited[right-1] and s[right]==s[right-2] and right>2):
                length+=1
                longest=max(length,longest)
            elif k>0:
                length+=1
                longest=max(length,longest)
                k-=1
                visited[right]=True
                # s[right]=s[right-1]
            
            else:
                left=right
                length=1                
            
            right+=1
        
        return longest 
                # longest+=1
                
            
            
        

        


print(Solution().characterReplacement("KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF",4))
