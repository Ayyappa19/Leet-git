class Solution {
public:
    vector<vector<int>> ans;
    void fun(vector<int> &a,int s,vector<int> &k,int t,int ind,int n){
        if(s>t) return;
        if (s==t){
            ans.push_back(k);
            return;
        }
        for( int i=ind;i<n;i++){
            if(ind!=i && a[i]==a[i-1]) continue;
            k.push_back(a[i]);
            fun(a,s+a[i],k,t,i+1,n);
            k.pop_back();
        }
        return;
    }
    vector<vector<int>> combinationSum2(vector<int>& cand, int target) {
        vector<int>k;
        sort(cand.begin(),cand.end());
        fun(cand,0,k,target,0,cand.size());
        return ans;
    }
};