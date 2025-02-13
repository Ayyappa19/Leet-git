class Solution {
public:
    bool solve(string & s){
        int i=0,j=s.size()-1;
        cout<<s;
        if(s.size()==1)return true;
        while(i<j){
            if(s[i]!=s[j]){
                // cout<<s[i]<<s[j]<<endl;
                return false;

            }
            i++;
            j--;
        }
        return true;
    }
    bool isPalindrome(string s) {
        string s1="";
        for( auto & x :s){
            if(isalnum(x)){
                x=tolower(x);
                s1+=x;
            }
        }
        cout<<s1;
        return solve(s1);
        
    }
};