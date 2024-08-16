class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # l=[]
        # for i in arrays:
        #     l+=i
        arrays.sort()
        # print(arrays)
        return abs(arrays[0][0]-arrays[-1][-1])
        
        