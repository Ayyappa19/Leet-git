class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        l = [0]*len(capacity)
        c = 0
        k = additionalRocks
        for i in range(len(capacity)):
            l[i] = capacity[i] - rocks[i]
        l.sort()
        for i in range(len(capacity)):
            if l[i] == 0 or k>=l[i]:
                c += 1
                k = k-l[i]
        return c
        