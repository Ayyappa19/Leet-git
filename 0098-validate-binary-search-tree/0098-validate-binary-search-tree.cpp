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
public:
    
    void solve(TreeNode* root,bool & k,long long &val){
        
        if(root->left!=NULL){
            solve(root->left,k,val);
        }
        long long z=root->val;
        if(val>=z){
            k=false;
            return ;
        }
        val=z;
        if(root->right!=NULL) solve(root->right,k,val);

    }
    bool isValidBST(TreeNode* root) {
        long long x=LLONG_MIN;
        bool k=true;
        if(root==NULL)return true;
        solve(root,k,x);
        return k;
    }
};