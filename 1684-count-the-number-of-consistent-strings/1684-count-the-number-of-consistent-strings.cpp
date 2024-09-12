#include<bits/stdc++.h>
class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        int c=0;
        map<char,int>m;
        for( int i=0;i<allowed.size();i++){
            if(m.find(allowed[i])!=m.end()){
                m[allowed[i]]+=1;
            }
            else{
                m[allowed[i]]=1;
            }
        }
        bool fi;
        for( int i=0;i<words.size();i++){
            fi=true;
            for( int j=0;j<words[i].size();j++){
                if (m.find(words[i][j])==m.end()){
                    fi=false;
                    break;
                }
            }
            if(fi){
                c+=1;
            }
        }
        return c;
    }
};