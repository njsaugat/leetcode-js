class Solution:
    def validAnagram(self,words):
        output={}
        for word in words:
            letters=[0]*26

            for char in word:
                
                diff=ord(char)-ord("a")
                letters[diff]+=1
                
                output[repr(letters)]=output.get(repr([letters]),[])
                output[repr(letters)].append(word)
        
        return [ value for  key,value in output.items()]
                