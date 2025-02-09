class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def solve(i,j,k,adj,x):
	        if(i<0 or j<0 or i>len(adj)-1 or j>len(adj[0])-1 or adj[i][j]!=x):
	            return
	        adj[i][j]=k
	        solve(i+1,j,k,adj,x)
	        solve(i-1,j,k,adj,x)
	        solve(i,j+1,k,adj,x)
	        solve(i,j-1,k,adj,x)
        if(image[sr][sc]==color):
            return image
        solve(sr,sc,color,image,image[sr][sc])
        return image
        
        


	    