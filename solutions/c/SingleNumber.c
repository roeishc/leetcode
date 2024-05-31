int singleNumber(int* nums, int numsSize) {
    
    int res = 0;
    for (int i = numsSize - 1; 0 <= i; i--)
        res ^= nums[i];

    return res;

}