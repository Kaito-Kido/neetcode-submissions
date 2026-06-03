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
    private int max = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        findSum(root);
        return max;
    }

    public int findSum(TreeNode node) {
        if (node.left == null && node.right == null) {
            max = Math.max(max, node.val);
            return node.val;
        }

        int sumLeft = 0;
        int sumRight = 0;

        if (node.left != null) sumLeft = findSum(node.left);
        if (node.right != null) sumRight = findSum(node.right);

        int horizonSum = node.val + Math.max(0, sumLeft) + Math.max(0, sumRight);
        int currentSum = node.val +  Math.max(Math.max(0, sumLeft), Math.max(0, sumRight));
        max = Math.max(horizonSum, max);
        max = Math.max(currentSum, max);

        return currentSum;
    }
}
