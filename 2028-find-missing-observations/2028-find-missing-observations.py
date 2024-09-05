class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        l=[0]*n
        x=((mean*(len(rolls)+n))-(sum(rolls)))
        k=x//n
        if x>6*n or x<n:
            return []
        r=x%n
        l=[k for i in range(n)]
        for i in range(r):
            l[i]+=1
        return l
        # if k>6:
        #     return []
        # if k*n==x and k<=6 and k>0:
        #     # print("hi")
        #     return [k for i in range(n)]
        # elif k*n<x and k<6 and k>0:
        #     l=[k for i in range(n)]
        #     nn=len(l)-1
        #     while(sum(l)<x and nn>=0):
                
        #         l[nn]+=1
        #     return l
        # else:
        #     return []



