class Solution:
    def productExceptSelf(self, a: List[int]) -> List[int]:
        p=1
        k=True
        c=0
        for i in range(0,len(a)):
            if(a[i]==0):
                k=False
                c+=1
                continue
            else:
                p*=a[i]
        for i in range(len(a)):
            if(a[i]==0 and c<2):
                a[i]=p
            elif(not k):
                a[i]=0
            else:
                a[i]=p//a[i]
        return a

         

        