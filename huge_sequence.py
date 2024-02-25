class Solution:
    def longest_sequence(self,nums):
        
        numset=set(nums) # [1,3,5,100,2,200]
        longest=0
        for num in numset:
            # check the start of the sequence
            # to be start of the sequence there should not be left num
            if (num-1) not in numset:
                length=1
                while (num+length) in numset:
                    length+=1
                
                longest=max(length,longest)

        return longest
    
print(Solution().longest_sequence([1,5,100,2,200,201,203,202,204]))
# blade is the template and the 