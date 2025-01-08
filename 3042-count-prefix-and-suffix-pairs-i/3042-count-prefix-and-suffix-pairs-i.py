class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        def checkPrefix(x, y):
            return x in y[len(y) - len(x):]
        def checkSuffix(x, y):
            return x in y[:len(x)]
        res = 0    
        for i in range(n):
            for j in range(i, n):
                if i != j:
                    if checkPrefix(words[i], words[j]) and checkSuffix(words[i], words[j]):
                        res+=1
        return res