class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        j=0
        l=[]
        processorTime.sort()
        tasks.sort(reverse=True)
        for i in range(len(tasks)):
            c=0
            t=processorTime[j]
            if (i+1)%4!=0:
                c+=(tasks[i]+t)
                l.append(c)
            else:
                c+=(tasks[i]+t)
                j+=1
                l.append(c)
        print(l)
        return max(l)