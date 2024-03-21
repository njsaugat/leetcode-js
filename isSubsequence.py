class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        while j<len(s):
            if i==len(t):
                return False
        
            if s[j]==t[i]:
                i+=1
                j+=1
            else:
                i+=1 
            
            

        return True
            # i+=1
            
print(Solution().isSubsequence("abc","ahbgdc"))