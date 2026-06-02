class Solution {
    private int count = 0;
    private int answer = 0;

    public int kthSmallest(TreeNode root, int k) {
        dfs(root, k);
        return answer;
    }

    private void dfs(TreeNode node, int k) {
        if (node == null) {
            return;
        }
        if (count >= k) return;

        dfs(node.left, k);

        count++;
        if (count == k) {
            answer = node.val;
            return;
        }

        dfs(node.right, k);
    }
}