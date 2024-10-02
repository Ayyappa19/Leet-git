class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        l=arr.copy()
        arr.sort()
        l2=[]
        d={}
        c=1
        for i in range(len(arr)):
            if arr[i] in d:
                pass
            else:
                d[arr[i]]=c
                c+=1
        for i in l:
            l2.append(d[i])
        return l2
        