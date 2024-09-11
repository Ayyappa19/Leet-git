class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        k=bin(start)
        x=bin(goal)
        c=0
        x=x[2::]
        k=k[2::]
        if len(x)>len(k):
            k=k.zfill(len(x))
        else:
            x=x.zfill(len(k))
        i=0
        while(i<len(k)):
            if k[i]!=x[i]:
                c+=1
            i+=1
        return c


        