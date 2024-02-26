class Solution:
    def merge_intervals(self,intervals):
        if len(intervals)==0:
            return intervals
        intervals.sort(key= lambda i: i[0])
        
        output=[intervals[0]]
        j=0
        for i in range(1,len(intervals)):
            
            curr_interval,prev_interval=intervals[i],output[j]
            start,end=0,1
            if curr_interval[start]<=prev_interval[end]:
                interval_end=max(curr_interval[end],prev_interval[end])
                output[j]=[prev_interval[start],interval_end]
                
            else:
                output.append(curr_interval)
                j+=1
        
        return output
    
    
print(Solution().merge_intervals([[1,2],[8,10],[2,6,]]))