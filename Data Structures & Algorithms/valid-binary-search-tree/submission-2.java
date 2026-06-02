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
    public boolean isValidBST(TreeNode root) {
        return dfs(root, -1001, 1001);
    }

    public boolean dfs(TreeNode node, int min, int max) {
        if (node.val >= max || node.val <= min) return false;

        if (node.left != null) {
            boolean leftResult = dfs(node.left, min, node.val);
            if (leftResult == false) return false;
        }

        if (node.right != null) {
            boolean rightResult = dfs(node.right, node.val, max);
            if (!rightResult) return false;
        }

        return true;
    }
}
