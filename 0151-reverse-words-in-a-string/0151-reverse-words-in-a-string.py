class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        l=list(s.split())
        k=""
        l=l[::-1]
        for i in range(len(l)-1):
            k+=l[i]
            k+=" "
        k+=l[-1]
        return k
        
        