int firstMissingPositive(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; i++){
        while (1 <= nums[i] && nums[i] <= numsSize && nums[nums[i]-1] != nums[i]){
            swap(nums, nums[i]-1, i);
        }
    }
    for (int i = 0; i < numsSize; i++){
        if (nums[i] != i + 1)
            return i + 1;
    }
    return numsSize + 1;
}

void swap(int* arr, int i, int j){
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}
