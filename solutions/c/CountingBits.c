/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int n, int* returnSize) {
    
    int* ans = (int*)malloc(sizeof(int) * (n + 1));
    if (!ans)
        return NULL;

    *returnSize = n + 1;
    ans[0] = 0;

    for (int i = 1; i < n + 1; i++)
        ans[i] = ans[i/2] + i % 2;

    return ans;

}