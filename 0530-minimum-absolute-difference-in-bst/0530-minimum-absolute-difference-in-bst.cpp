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
    void solve(TreeNode* root,int &k,int &m){
        
        if(root == NULL){
            return ;
        }
        solve(root->left,k,m);
        if(k!=-1){
            m=min(m,(root->val-k));
        }
        k = root->val;
        solve(root->right,k,m);
    }
    int getMinimumDifference(TreeNode* root) {
        int m = INT_MAX;
        int k=-1;
        solve(root,k,m);
        return m;
    }
};