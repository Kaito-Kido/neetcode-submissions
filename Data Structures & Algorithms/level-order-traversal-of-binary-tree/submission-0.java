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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;
        dfs(result, root, 0);
        return result;
    }

    public void dfs(List<List<Integer>> result, TreeNode node, int level) {
        if (result.size() == level) result.add(new ArrayList<Integer>());

        result.get(level).add(node.val);
        if (node.left != null)
            dfs(result, node.left, level + 1);
        if (node.right != null)
            dfs(result, node.right, level + 1);
    }
}
