/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool evaluateTree(struct TreeNode* root) {
    switch(root->val){
        case 0:
        case 1:
            return root->val;
        case 2:
            return evaluateTree(root->left) || evaluateTree(root->right);
        case 3:
            return evaluateTree(root->left) && evaluateTree(root->right);
        default:
            return 0;
    }
}