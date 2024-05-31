int singleNumber(int* nums, int numsSize) {

    int ones, twos;
    ones = twos = 0;

    for (int i = 0; i < numsSize; i++){
        ones = ones ^ nums[i] & ~twos;
        twos = twos ^ nums[i] & ~ones;
    }

    return ones;

}