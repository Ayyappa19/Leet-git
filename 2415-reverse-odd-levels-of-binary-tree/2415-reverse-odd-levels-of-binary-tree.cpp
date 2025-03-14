/**
 * Definition for a binary tree node->
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
    void leveling(TreeNode* lefty,TreeNode* righty,int level){
        if(lefty==NULL || righty==NULL)return ;
        if(level%2){
            int val=lefty->val;
            lefty->val=righty->val;
            righty->val=val;

        }
        leveling(lefty->left,righty->right,level+1);
        leveling(lefty->right,righty->left,level+1);
    }
    TreeNode* reverseOddLevels(TreeNode* root) {
        if(root==NULL)return root;
        leveling(root->left,root->right,1);
        return root;
    }
};