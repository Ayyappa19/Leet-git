class Solution:
    def numOfUnplacedFruits(self, f: List[int], b: List[int]) -> int:
        n=len(f)
        check=[False]*n
        k=0
        for i in f:
            x=False
            for j in range(n):
                if not check[j] and b[j]>=i:
                    check[j]=True
                    x=True
                    break
            if not x:
                k+=1
        return k
        