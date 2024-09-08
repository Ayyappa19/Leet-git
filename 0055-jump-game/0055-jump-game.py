class Solution:
    def canJump(self, arr: List[int]) -> bool:
        n = len(arr)
        x = y = z = 0
    
        for i in range(n-1):
            x = max(x, arr[i]+i)
            if i == y:
                y = x
                i = x
                z +=1
    
        if y >= n-1:
            return True
        return False
    
        