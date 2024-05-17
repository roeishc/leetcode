/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
typedef struct TreeNode Node;
struct TreeNode* removeLeafNodes(struct TreeNode* root, int target) {
    if (root->left)
        root->left = removeLeafNodes(root->left, target);
    if (root->right)
        root->right = removeLeafNodes(root->right, target);
    if (!root->left && !root->right && root->val == target){
        free(root);
        return NULL;
    }
    return root;
}