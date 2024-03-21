class Solution:
    
    def findTotalDifferences(self,nums,k):
        
        # nums.sort()

        hashset=set(nums)
        count=0
        for num in hashset:
            if num+k in hashset:
                count+=1

            # hashset.add(num)
        return count
        
        
            


        
print(Solution().findTotalDifferences(nums=[1, 7, 5,9, 2, 12, 3],k=2))
