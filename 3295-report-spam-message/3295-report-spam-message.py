class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        d = {}
        l = []
        for i in message:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in bannedWords:
            if i in d:
                l.append(d[i])
        if sum(l)>=2:
            return True
        return False
       