class Solution:
    def sortVowels(self, s: str) -> str:
        v="aeiouAEIOU"
        s1=[i for i in s if i in v]
        s1.sort()

        l=[]
        j=0
        for ch in s:
            if ch in v:
                l.append(s1[j])
                j+=1
            else:
                l.append(ch)
        
        return "".join(l)
