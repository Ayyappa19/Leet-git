class Solution:
    def dividePlayers(self, l: List[int]) -> int:
        k=len(l)//2
        c=sum(l)//k
        res=0
       
        
        if sum(l)%c==0 :
            l=sorted(l)
           
            i=0
            j=len(l)-1

            while i<j:
                if l[i]+l[j]==c:
                    res+=(l[i]*l[j])
                else:
                    return -1
                i+=1
                j-=1
           
               
            return res
            
        else:
            return -1
        