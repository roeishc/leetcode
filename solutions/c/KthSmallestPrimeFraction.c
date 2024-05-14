/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* kthSmallestPrimeFraction(int* arr, int arrSize, int k, int* returnSize) {
    double left = 0, right = 1.0, mid, maxFraction, tempFraction;
    int total, numeratorIdx, denominatorIdx, j;
    *returnSize = 2;
    int* result = (int*)malloc(sizeof(int) * (*returnSize));
    if (!result)
        return NULL;

    while (left < right) {
        mid = (left + right) / 2;
        maxFraction = 0.0;
        total = numeratorIdx = denominatorIdx = 0;
        j = 1;

        for (int i = 0; i < arrSize - 1; i++) {
            while (j < arrSize && mid * arr[j] <= arr[i])
                j++;

            total += arrSize - j;

            if (j == arrSize)
                break;

            tempFraction = (double)arr[i] / arr[j];

            if (maxFraction < tempFraction) {
                numeratorIdx = i;
                denominatorIdx = j;
                maxFraction = tempFraction;
            }
        }

        if (total == k) {
            result[0] = arr[numeratorIdx];
            result[1] = arr[denominatorIdx];
            return result;
        }
        else if (total < k)
            left = mid;
        else
            right = mid;
    }

    *returnSize = 0;
    free(result);
    return NULL;
}