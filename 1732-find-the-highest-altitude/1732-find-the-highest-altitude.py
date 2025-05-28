class Solution:
    def largestAltitude(self, gain):
        m=0
        k=0
        for i in gain:
            k+=i
            m=max(m,k)
        return m