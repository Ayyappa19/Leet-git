class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i,j=0,0
        k=False
        s=""
        if(ch not in word):
            return word
        while(j<len(word)):
            if(k):
                s+=word[j]
            elif(word[j]==ch):
                # print(word[j::-1])
                s+=word[j::-1]
                k=True
            j+=1
        return s
        
        