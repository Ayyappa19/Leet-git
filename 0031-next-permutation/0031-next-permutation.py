class Solution:
    def nextPermutation(self, s: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # return []
        i = len(s)-2
        while i>=0 and s[i+1]<=s[i]:
            i-=1
        if i>=0:
            j=len(s)-1
            while(s[j]<=s[i]):
                j-=1
            s[i],s[j]=s[j],s[i]
        k=s[i+1:]
        
        s[::]=s[:i+1]+k[::-1]
        