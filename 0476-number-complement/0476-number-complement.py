class Solution:
    def findComplement(self, num: int) -> int:
        s=bin(num)
        print(s)
        s=s[2::]
        k=""
        for i in range(len(s)):
            if s[i]=='0':
                k+='1'
            else:
                k+='0'
        n=0
        for i in range(len(k)-1,-1,-1):
            n+=(int(k[i]))*(2**(((len(k)-1)-i)))
            print(k)
            # print(type(int(k[i])))
        return n

        