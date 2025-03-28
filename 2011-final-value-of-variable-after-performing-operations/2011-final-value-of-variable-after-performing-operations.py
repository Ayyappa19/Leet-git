class Solution:
    def finalValueAfterOperations(self, o: List[str]) -> int:
        c=0
        for i in o:
            if i=='--X'or i== 'X--':
                c-=1
            else:
                c+=1
        return c
        