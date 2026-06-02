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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode left;
        TreeNode right;
        if (p.val < q.val) {
            left = p;
            right = q;
        } else {
            left = q;
            right = p;
        }
        if (left.val < root.val && root.val < right.val) return root;
        if (left.val == root.val) return left;
        if (right.val == root.val) return right;
        if (root.val < left.val) return lowestCommonAncestor(root.right, left, right);
        return lowestCommonAncestor(root.left, left, right);
    }
}
