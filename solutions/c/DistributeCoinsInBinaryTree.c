/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

struct Result {
    int coins;
    int moves;
};

struct Result dfs(struct TreeNode* current) {
    if (!current)
        return (struct Result){0, 0};

    struct Result leftResult = dfs(current->left);
    struct Result rightResult = dfs(current->right);

    int coins = current->val + leftResult.coins + rightResult.coins - 1;
    int moves = abs(leftResult.coins) + abs(rightResult.coins) + leftResult.moves + rightResult.moves;

    return (struct Result){coins, moves};
}

int distributeCoins(struct TreeNode* root) {
    struct Result result = dfs(root);
    return result.moves;
}
