class Solution {
public:
    void solve(int i,int j, int t,vector<vector<int>>& mat, int n,int m){
        if(i<0 or i>n-1 or j<0 or j>m-1 or mat[i][j]==0 or(mat[i][j]<t and mat[i][j]>1))
            return;
        mat[i][j] = t;
        solve(i+1,j,t+1,mat,n,m);
        solve(i-1,j,t+1,mat,n,m);
        solve(i,j+1,t+1,mat,n,m);
        solve(i,j-1,t+1,mat,n,m);
    }
    int orangesRotting(vector<vector<int>>& mat) {
        // Code here
        int t=2,s=2;
        int n=mat.size();
        int m=mat[0].size();
        for( int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(mat[i][j]==2)
                solve(i,j,2,mat,n,m);
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                // cout<<mat[i][j]<<" ";
                if(mat[i][j]==1)
                return -1;
                s=max(s,mat[i][j]);
            }
        }
        return s-t;
    }
};