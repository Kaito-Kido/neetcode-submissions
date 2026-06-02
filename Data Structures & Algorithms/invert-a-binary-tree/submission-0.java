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
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return root;
        Queue<TreeNode> queue = new ArrayDeque<>();
        TreeNode cursor;
        TreeNode temp;
        queue.add(root);

        while(!queue.isEmpty()) {
            cursor = queue.poll();
            temp = cursor.left;
            cursor.left = cursor.right;
            cursor.right = temp;
            if (cursor.left != null)
                queue.add(cursor.left);
            if (cursor.right != null)
                queue.add(cursor.right);
            
        }

        return root;
    }
}
