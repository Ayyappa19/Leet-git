class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def solve(k):
            print(k)
            visited[k]=True
            for i in range(len(isConnected)):
                if(isConnected[k][i]==1 and not visited[i]):
                    solve(i)
        count = 0
        visited = [False] * len(isConnected)
        print(visited)
        for i in range(len(isConnected)):
            if(not visited[i]):
                count +=1
                print(i)
                solve(i)
        return count