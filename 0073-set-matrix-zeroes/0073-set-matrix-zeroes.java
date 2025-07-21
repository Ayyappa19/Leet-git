class Solution {
    public void setZeroes(int[][] mat) {
        boolean firstrow=false;
        boolean firstcol=false;
        int n=mat.length, m=mat[0].length;
        for( int i=0;i<n;i++){
            if(mat[i][0]==0){
                firstrow=true;
            }
        }
        for( int j=0;j<m;j++){
            if(mat[0][j]==0){
                firstcol=true;
            }
        }
        for( int i=1;i<n;i++){
            for( int j=1;j<m;j++){
                if(mat[i][j]==0){
                    mat[i][0]=0;
                    mat[0][j]=0;
                }
            }

        }
        for(int i=1;i<n;i++){
            for( int j=1;j<m;j++){
                if(mat[i][0]==0 || mat[0][j]==0){
                    mat[i][j]=0;
                }
            }
        }
        if(firstcol){
            for( int i=0;i<m;i++){
                mat[0][i]=0;
            }
        }
        if(firstrow){
            for( int i=0;i<n;i++){
                mat[i][0]=0;
            }
        }
        
    }
}