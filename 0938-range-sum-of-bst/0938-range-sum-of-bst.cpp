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
    int sum=0;
    void summing(TreeNode* root,int low,int high){
        if(root==NULL) return ;
        if(root->val>=low && root->val<=high){
            sum+=root->val;
        }
        summing(root->left,low,high);
        summing(root->right,low,high);
    }
    int rangeSumBST(TreeNode* root, int low, int high) {

        if(root == NULL)return 0;
        summing(root,low,high);
        return sum;
        
        
    }
};