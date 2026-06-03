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

public class Codec {
    private int index = 0;

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) return "";
        ArrayList<String> listString = new ArrayList<>();
        dfs(root, listString);
        System.out.println(listString);
        return String.join(",", listString);
    }

    public void dfs(TreeNode node, ArrayList<String> listString) {
        if (node == null) {
            listString.add("N");
            return;
        }

        listString.add(String.valueOf(node.val));
        dfs(node.left, listString);
        dfs(node.right, listString);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data == "") return null;
        String[] listString = data.split(",");

        return build(listString);
    }

    public TreeNode build(String[] listString) {
        String currentVal = listString[index];

        if ("N".equals(currentVal)) {
            return null;
        }
        TreeNode node = new TreeNode(Integer.valueOf(currentVal));
        if (index + 1 < listString.length) {
            index++;
            node.left = build(listString);
        }

        if (index + 1 < listString.length) {
            index++;
            node.right = build(listString);
        }

        return node;
    }
}
