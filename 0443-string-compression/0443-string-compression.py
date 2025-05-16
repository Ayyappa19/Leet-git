class Solution:
    def compress(self, chars: List[str]) -> int:
        # d={}
        # for i in chars:
        #     if i in d:
        #         d[i]+=1
        #     else:
        #         d[i]=1
        # c=0
        # print(d)
        # for i in d.values():
        #     if i >1:
        #         c+=len(str(i))+1
        #     else:
        #         c+=1
        # return c
        i,j=0,0
        while(j<len(chars)):
            x=chars[j]
            c=0
            while(j<len(chars) and chars[j]==x):
                j+=1
                c+=1
            chars[i]=x
            i+=1
            if c>1:
                for k in str(c):
                    chars[i]=k
                    i+=1
        return i