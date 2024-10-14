class Solution {
public:
    long long maxKelements(vector<int>& num, int k) {
        long long s=0;
        priority_queue<int> arr;
        for ( int i:num)
        arr.push(i);
        
        while(k){
            int x=arr.top();
            // cout<<x<<" "<<"hi";
            s+=x;
            arr.pop();
            float x1=x+0.0;
            arr.push(ceil(x1/3));
            
            k-=1;
        }
        return s;
        
    }
};