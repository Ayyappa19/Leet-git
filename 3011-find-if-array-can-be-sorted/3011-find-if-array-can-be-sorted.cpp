class Solution {
public:
    int cnts(int n){
        int c=0;
        while(n!=0){
            n=n&n-1;
            c+=1;
            
        }
        return c;
    }
    bool canSortArray(vector<int>& a) {
            for(int i=0;i<a.size()-1;i++){
                for (int j = 0; j < a.size() - i - 1; j++) {
                    if (a[j] > a[j + 1]) {
                        if (cnts(a[j])!=cnts(a[j+1]))
                            return false;
                         swap(a[j],a[j+1]);
                    }
            }
         }
            return true;
    }
};