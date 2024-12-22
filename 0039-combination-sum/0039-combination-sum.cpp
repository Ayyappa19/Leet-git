class Solution {
public:
    vector<vector<int>>ans;
    map<vector<int>,int>mp;
    vector<int>v;
    void solve(int k,vector<int>& c,int sum,int x){
        if(sum==x){
            if(mp.find(v)==mp.end()){
                ans.push_back(v);
                mp[v]++;
            }
            return;
        }
        for(int i=k;i<c.size();i++){
            if(sum+c[i]<=x){
                v.push_back(c[i]);
                solve(i,c,sum+c[i],x);
                v.pop_back();
            }
        }
    }
    vector<vector<int>> combinationSum(vector<int>& c, int t) {
        solve(0,c,0,t);
        return ans;
        
    }
};