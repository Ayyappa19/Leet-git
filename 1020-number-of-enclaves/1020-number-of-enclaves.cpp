class Solution {
public:
    void solve(vector<vector<int>>& grid, int i, int j){
        if(i<0 || j<0 || i>=grid.size() || j>=grid[i].size() || grid[i][j]!=1){
            return;
        }
        grid[i][j]=0;
        solve(grid,i+1,j);
        solve(grid,i-1,j);
        solve(grid,i,j+1);
        solve(grid,i,j-1);
    }
    int numEnclaves(vector<vector<int>>& grid) {
        int c=0, m=grid.size(), n=grid[0].size();
        for(int i=0;i<m;++i){
            for(int j=0;j<n;++j){
                if((i==0 or j==0 or i==m-1 or j==n-1)){
                    solve(grid,i,j); 
                }
            }
        }
        for(int i=0;i<m;++i){
            for(int j=0;j<n;++j){
                if(grid[i][j]==1)
                    c++;
            }
        }
        return c;
    }
};