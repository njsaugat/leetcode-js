class Solution:
    def lengthOfLongestSubstring(self, s) :
        if len(s)==0:
            return 0
        left,right=0,0
        hashset={}
        max_length=1
        while right<len(s):

            if s[right] in hashset:
                left=hashset[s[right]]+1
                hashset={}
                while left<right:
                    hashset[s[left]]=left
                    left+=1
            
                
            
            # longest+=s[left]
            hashset[s[right]]=right
            max_length=max(max_length,len(hashset))
            right+=1
        
        return max_length
            


print(Solution().lengthOfLongestSubstring("pwasdwuiovp"))