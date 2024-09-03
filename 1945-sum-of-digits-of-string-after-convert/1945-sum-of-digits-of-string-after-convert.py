class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s1=''
        for i in s:
            # print(ord(i),end=" ")
            s1+=str(ord(i)-96)
            
        # print(s1)
        for j in range(k):
            z=0
            for i in s1:
                z+=int(i)
            s1=str(z)
        return z

        