class Solution:
    def isPalindrome(self, s: str) -> bool:
        si=""
        for i in s:
            if i.isalnum():
                si+=i.lower()
        # print(si)
        # k=0
        i,j=0,len(si)-1
        while(i<j):
            if si[i]!=si[j]:
                return False
            i+=1
            j-=1
        return True