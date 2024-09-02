class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        z=sum(chalk)
        while(k>=z):
            k%=z
        i=0
        # print(k)
        while(k>=0):
            # print(i,k)
            if k<=0:
                break
            if k<chalk[i]:
                break
            k-=chalk[i]
            
            i+=1
        return i
            
        