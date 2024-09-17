class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d={}
        l=s1.split(" ")
        l1=s2.split(" ")
        for i in l:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in l1:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ans=[]
        for i in d.keys():
            if d[i]==1:
                ans.append(i)
        return ans
        