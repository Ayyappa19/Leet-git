class Solution {
private:
    void depthCheck(vector<vector<char>>& grid, int i, int j) {
        if (i<0 || j<0 || i>grid.size()-1 || j>grid[0].size()-1) return;
        if (grid[i][j]=='1') {
            grid[i][j]='0';
            depthCheck(grid, i-1, j);
            depthCheck(grid, i, j-1);
            depthCheck(grid, i+1, j);
            depthCheck(grid, i, j+1);
        } else return;
    }
public:
    int numIslands(vector<vector<char>>& grid) {
        int res=0;
        for (int i=0; i<grid.size(); i++) {
            for (int j=0; j<grid[0].size(); j++) {
                if (grid[i][j]=='1') {
                    depthCheck(grid, i, j);
                    res++;
                }
            }
        }
        return res;
    }
};