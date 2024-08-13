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
    vector<int>a{0};
    void solve(TreeNode* root,int k,int s){
        if (root==NULL) return;

        if (root->left==NULL and root->right==NULL){
            s+=root->val;
        if(s==k){
            cout<<s;
            a[0]=1;
            return ;
        }
        }
        cout<<s;
        solve(root->left,k,s+root->val);
        // s-=root->val;
        solve(root->right,k,s+root->val);

    }
    bool hasPathSum(TreeNode* root, int targetSum) {
        solve(root,targetSum,0);
        return 1==a[0];
    }
};