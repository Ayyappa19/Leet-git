/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    vector<int> v;
public:
    void avg(TreeNode * root,int c,int s){
        if (root==NULL){
            if (v.size()==0){
                v.push_back(s);
                v.push_back(c);
            }
            else{
                v.pop_back();
                v.pop_back();
                v.push_back(s);
                v.push_back(c);
            }
        }
        else{
            s+=root->val;
            avg( root->left,c+1,s);
            avg( root->right,c+1,s);
        }
        

    }
    int averageOfSubtree(TreeNode* root) {
        avg(root,0,0);
        int k;
        k=v[0]/v[1];
        return k;

        
    }
};