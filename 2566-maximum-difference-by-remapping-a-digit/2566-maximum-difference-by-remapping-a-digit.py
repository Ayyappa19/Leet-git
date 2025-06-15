class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        maxii=s
        for i in s:
            if i!='9':
                maxii=s.replace(i,'9')
                break

        minii=s
        for i in s:
            if i!='0':
                minii=s.replace(i,'0')
                break

        return int(maxii)-int(minii)