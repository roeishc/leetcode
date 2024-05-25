/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int rangeSumBST(struct TreeNode* root, int low, int high) {
    
    if (!root)
        return 0;
    int res = low <= root->val && root->val <= high ? root->val : 0;
    if (low <= root->val)
        res += rangeSumBST(root->left, low, high);
    if (root->val <= high)
        res += rangeSumBST(root->right, low, high);
    return res;

}