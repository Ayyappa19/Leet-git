/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private int m=0;
    public int checker(TreeNode root) {
        if(root==null) return 0;
        // System.out.println(m);
        int l=checker(root.left);
        // System.out.println(m);
        int r=checker(root.right);
        // System.out.println(m);
        m=Math.max(m,l+r);
        System.out.println(m);
        
        return Math.max(l,r)+1;
        
    }
    public int diameterOfBinaryTree(TreeNode root){
        checker(root);
        return m;

    }
}