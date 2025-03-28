class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        c = 0 
        d = {}
        for i in range(len(garbage)) : 
            c += len(garbage[i])
            if 'G' in garbage[i] : 
                d['G'] = i
            if 'P' in garbage[i] : 
                d['P'] = i
            if 'M' in garbage[i] : 
                d['M'] = i
        
        for key in d.keys() : 
            c += sum(travel[:d[key]])
            
        return c 