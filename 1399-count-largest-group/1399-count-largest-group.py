class Solution:
    def countLargestGroup(self, n: int) -> int:
        d={}
        for i in range(1,n+1):
            x=sum(int(x) for x in str(i))
            if x not in d:
                d[x]=[]
            d[x].append(i)
        maxs=0
        for i in d:
            if len(d[i])>maxs:
                maxs=len(d[i])
        c=0
        for i in d:
            if len(d[i])==maxs:
                c+=1
        return c