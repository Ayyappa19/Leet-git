class Solution:
    def kthCharacter(self, k: int) -> str:
        x="a"
        while len(x)<k:
            s="" 
            for c in x: 
                s1=chr(((ord(c)-ord('a')+1)%26)+ord('a'))
                s+=s1
            x+=s
        return x[k-1]
            
        