class Solution:
    def eraseOverlapIntervals(self, intervals) :
        intervals.sort(key=lambda i:i[0])

        maxRemove=0
        i=1
        while i<len(intervals):
            start,end=0,1
            currInterval,prevInterval=intervals[i],intervals[i-1]
            if currInterval[start]<prevInterval[end]<currInterval[end]:
                maxRemove+=1
                i+=1
            if currInterval==prevInterval:
                maxRemove+=1
                # i+=1
            i+=1
        return maxRemove



    def eraseOverlapIntervals(self,intervals):
        intervals.sort()

        res=0
        prevEnd=intervals[0][1]

        for start,end in intervals[1:]:
            if start>=prevEnd:
                prevEnd=end
            else:
                res+=1
                prevEnd=min(end,prevEnd)
        
        return res
    
    
    def eraseOverlapIntervals(self,intervals):
        
        intervals.sort()
        res=0
        prevEnd=intervals[0][1]

        for start,end in intervals[1:]:
            if start>=prevEnd:
                prevEnd=end
            else:
                res+=1
                prevEnd=min(end,prevEnd)
        
        return res
    
    def eraseOverlapIntervals(self,intervals):
        
        intervals.sort()
        res=0

        prevEnd=intervals[0][1]

        for start,end in intervals[1:]:
            if start>=prevEnd:
                prevEnd=end
            else:
                res+=1
                prevEnd=min(end,prevEnd)
        
        return res
    
    
            
print(Solution().eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))