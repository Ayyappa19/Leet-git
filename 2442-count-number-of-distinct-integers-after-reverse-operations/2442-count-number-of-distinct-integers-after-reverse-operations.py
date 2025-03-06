class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def rev(n):
            k=0
            while(n):
                r=n%10
                k=k*10+r
                n//=10
            return k

        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
            k=rev(i)
            if k in d:
                d[k]+=1
            else:
                d[k]=1
        return len(d)

        