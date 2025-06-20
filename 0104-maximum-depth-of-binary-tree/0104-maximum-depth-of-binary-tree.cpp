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
    int ans=0;
    void solve(TreeNode* root,int h){
        if(!root) return;

        ans=max(ans,h);

        solve(root->left,h+1);
        solve(root->right,h+1);
    }
    int maxDepth(TreeNode* root) {
        if(!root) return 0;
        solve(root,0);
        return ans+1;
    }
};