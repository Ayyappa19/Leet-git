// #include<bits/stdc++.h>
class Solution {
public:
    void rotate(vector<vector<int>>& a) {
        int n=a.size();
        int k=n;
        vector<vector<int>>v(n,vector<int>(n,0));
        for(int i=0;i<n;i++){
            for (int j=0;j<n;j++){
                v[j][n-i-1]=a[i][j];
            }
        }
        for (int i=0;i<n;i++){
            for( int j=0;j<n;j++){
            a[i][j]=v[i][j];}
        }
        
    }
};  