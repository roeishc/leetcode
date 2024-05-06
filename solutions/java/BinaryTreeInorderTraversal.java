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
class BinaryTreeInorderTraversal {
    public List<Integer> inorderTraversal(TreeNode root) {
        
        List<Integer> list = new ArrayList<>();
        if (root == null)
            return list;

        if (root.left != null)
            list.addAll(inorderTraversal(root.left).stream().collect(Collectors.toList()));
        list.add(root.val);
        if (root.right != null)
            list.addAll(inorderTraversal(root.right).stream().collect(Collectors.toList()));

        return list;

    }
}