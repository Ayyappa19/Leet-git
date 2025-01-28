class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        if len(s)==0:
            return 0
        else:
            a="1234567890+-"
            if s[0] not in a :
                return 0
            else:
                k=""
                for i in range(len(s)):
                    if s[i]=='-' and len(k)==0:
                        k+=s[i]
                    elif s[i]=='+' and len(k)==0:
                        k+=s[i]
                    elif s[i]==" ":
                        break
                    elif s[i]=='-' and len(k)!=0:
                        break
                    elif s[i]=='+' and len(k)!=0:
                        break
                    elif s[i].isdigit():
                        k+=s[i]
                    elif s[i] not in a:
                        break
                if len(k)==0:
                    return 0
                elif len(k)==1 and (s[0]=='+' or s[0]=='-'):
                    return 0
                elif int(k) < -2**31:
                    return -2**31
                elif int(k) > (2**31)-1:
                    return (2**31)-1
                else:
                    return int(k)
            
        