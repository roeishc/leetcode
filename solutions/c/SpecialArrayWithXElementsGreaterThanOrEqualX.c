#define min(a, b) a <= b ? a : b

int specialArray(int* nums, int numsSize) {

    int* freq = (int*)calloc(numsSize + 1, sizeof(int));
    if (!freq)
        exit(1);

    int i, suffixSum;

    for (i = 0; i < numsSize; i++)
        freq[min(numsSize, nums[i])]++;

    suffixSum = 0;
    for (; 0 < i; i--){
        suffixSum += freq[i];
        if (suffixSum == i)
            return suffixSum;
    }

    return -1;

}