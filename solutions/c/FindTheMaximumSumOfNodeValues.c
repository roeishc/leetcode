#define max(a, b) (b < a) ? a : b
#define min(a, b) (a < b) ? a : b

long long maximumValueSum(int* nums, int numsSize, int k, int** edges, int edgesSize, int* edgesColSize) {
    long long sum = 0;
    int count, positiveMinimum, negativeMaximum, operatedNodeValue, netChange;
    count = 0;
    positiveMinimum = INT_MAX;
    negativeMaximum = INT_MIN;
    for (int i = 0; i < numsSize; i++){
        operatedNodeValue = nums[i] ^ k;
        sum += nums[i];
        netChange = operatedNodeValue - nums[i];
        if (0 < netChange){
            positiveMinimum = min(positiveMinimum, netChange);
            sum += netChange;
            count++;
        }
        else
            negativeMaximum = max(negativeMaximum, netChange);
    }
    if (count % 2 == 0)
        return sum;
    return max(sum - positiveMinimum, sum + negativeMaximum);
}