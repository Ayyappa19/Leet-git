class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:return []
        else:
            di = {'2': 'abc','3': 'def','4': 'ghi','5': 'jkl','6': 'mno','7': 'pqrs','8':'tuv','9': 'wxyz'};
            a = ['']
            for i in digits:
                s = []
                for j in di[i]:
                    for k in a:
                        s+=[k+j]
                a = s
            return a