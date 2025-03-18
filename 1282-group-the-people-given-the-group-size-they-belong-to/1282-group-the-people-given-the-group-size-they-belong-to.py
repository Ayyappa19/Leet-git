class Solution:
    def groupThePeople(self, g: List[int]) -> List[List[int]]:
        d={}
        for i in range(len(g)):
            if g[i] not in d:
                d[g[i]]=[i]
            else:
                d[g[i]].append(i)
        l=[]
        for i in d.keys():
            if len(d[i])==i:
                l.append(d[i])
            else:
                k=0
                for _ in range(len(d[i])//i):
                    l.append(d[i][k:k+i])
                    # print(d[i])
                    # print(d[i][k:k+i])
                    k=k+i
        return l

            

        
        