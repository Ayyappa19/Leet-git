class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        l = []
        i = 1
        
        for num in target:
            while i < num:
                l.append("Push")
                l.append("Pop")
                i += 1
            l.append("Push")
            i += 1
        
        return l