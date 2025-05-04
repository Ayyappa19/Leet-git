class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        d={}
        c=0
        for i in range(len(dominoes)):
            dominoes[i] = sorted(dominoes[i])
        for i in dominoes:
            if str(i) not in d:
                d[str(i)]=1
            else:
                d[str(i)]+=1
        for i in d:
            if d[i]>1:
                c+=(d[i]*(d[i]-1))//2            
        return c
            
                
                
                