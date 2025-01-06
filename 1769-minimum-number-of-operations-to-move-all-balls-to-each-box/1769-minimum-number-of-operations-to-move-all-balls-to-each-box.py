class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n=len(boxes)
        l=[int(box) for box in boxes]
        res=[0]*n
        c,s1=0,0
        for i in range(n):
            res[i]+=s1
            c+=l[i]
            s1+=c
        c,s1=0,0
        for i in range(n-1,-1,-1):
            res[i]+=s1
            c+=l[i]
            s1+=c
        
        return res



