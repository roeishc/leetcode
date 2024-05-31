/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* singleNumber(int* nums, int numsSize, int* returnSize) {
    
    int xorTotal, i, lsbDiff;
    xorTotal = i = 0;
    *returnSize = 2;
    int* res;
    assert(res = (int*)calloc(*returnSize, sizeof(int)));
    
    for (; i < numsSize; i++)
        xorTotal ^= nums[i];

    
    /*
    - find the LSB in xorTotal which is set to 1.
      reminder: two's complement to get the negation of x
      requires flipping all bits of x and adding 1.
      bitwise AND between x and -x (after applying two's compelemt negation)
      yields the LSB which is set to 1 in x.
    - using unsigned int for the edge case of xorTotal == INT_MIN
    */
    lsbDiff = xorTotal & -(unsigned int)xorTotal;

    for (i = 0; i < numsSize; i++){
        if ((nums[i] & lsbDiff) == 0)
            res[0] ^= nums[i];
        else
            res[1] ^= nums[i];
    }
    
    return res;

}