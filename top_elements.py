class Solution:
    def topKFrequent(self,nums,k):
        hashset={}
        res=[]
        frequencies=[[]for i in range(len(nums)+1)]

        for num in nums:
            hashset[num]=1+hashset.get(num,0)
        
        for num,count in hashset.items():
            frequencies[count].append(num)
        
        for i in range(len(frequencies)-1,-1,-1):
            for frequency in frequencies[i]:
                res.append(frequency)
                if len(res)==k:
                    return res
         
        # return res       
        
                
print(Solution().topKFrequent([1,1,1,1,3,5,5,5,5,1,],1))