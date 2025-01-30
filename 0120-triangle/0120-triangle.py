class Solution:
    def minimumTotal(self, t: List[List[int]]) -> int:
        s=0
        if(len(t)==1):
            return min(t[0])
        # l=[]
        for i in range(len(t)-2,-1,-1):
            # l1=[]
            for j in range(i+1): 
                # print(j)
                t[i][j]=(min((t[i][j]+t[i+1][j]),(t[i][j]+t[i+1][j+1])))
            
        print(t)
        # return(min())
        return t[0][0]
                
            
            
                        