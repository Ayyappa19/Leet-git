class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        d={}
        if(k>len(s)):
            return False
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        c=0
        # print(d)
        for i in d.keys():
            if(d[i]%2==1):
                c+=1
        # print(d,c)
        return c<=k 
            
        
        