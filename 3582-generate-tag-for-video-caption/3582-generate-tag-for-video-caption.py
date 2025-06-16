class Solution:
    def generateTag(self, caption: str) -> str:
        s="#"
        l=caption.split(" ")
        for i in l:
            if s[-1]=='#':
                s+=i.lower()
                # print(s)
            else:
                s+=i[0:1].upper()+i[1:].lower()
        # print(s)
        return s[:100]
        