class Solution:
    def is_valid(self,word1,word2):
        hashset1={}
        hashset2={}
        for char in word1:
            hashset1[char]=1+hashset1.get(char,0)
        for char in word2:
            hashset2[char]=1+hashset2.get(char,0)
        
        
        return hashset1==hashset2
    
    
    
print(Solution().is_valid('ant','tani'))
print(swap('a'))