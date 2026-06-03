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
    private HashMap<Integer, Integer> valToIndexMap = new HashMap<>();

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        for (int i = 0; i < inorder.length; i++) {
            valToIndexMap.put(inorder[i], i);
        }
        return build(preorder, 0, 0, preorder.length - 1);
    }

    public TreeNode build(
            int[] preorder, 
            int preIndex, 
            int inLeftIndex,
            int inRightIndex
        ) {
        if (inLeftIndex > inRightIndex) return null;
        int nodeVal = preorder[preIndex];
        int inIndex = valToIndexMap.get(nodeVal);
        int leftSize = inIndex - inLeftIndex;
        TreeNode node = new TreeNode(nodeVal);
        TreeNode leftNode = build(preorder, preIndex + 1, inLeftIndex, inIndex - 1);
        TreeNode rightNode = build(preorder, preIndex + 1 + leftSize, inIndex + 1, inRightIndex);
        node.left = leftNode;
        node.right = rightNode;
        return node;
    }
}
