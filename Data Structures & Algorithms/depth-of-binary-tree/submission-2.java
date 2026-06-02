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
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;

        int level = 0;
        Queue<TreeNode> queue = new ArrayDeque<>();
        TreeNode current;
        queue.add(root);

        while(!queue.isEmpty()) {
            int queueSize = queue.size();
            level++;
            for (int i = 0; i < queueSize; i++) {
                current = queue.poll();
                if (current.left != null) queue.add(current.left);
                if (current.right != null) queue.add(current.right);
            }
        }

        return level;
    }
}
