int findDuplicate(int* nums, int numsSize) {

    int tortoise, hare;
    tortoise = hare = nums[0];

    do {
        tortoise = nums[tortoise];
        hare = nums[nums[hare]];
    }
    while (tortoise != hare);

    /*
    after the loop, the tortoise is at the first intersection.
    according to Floyd, the distance between the first node
    to the start of the cycle, is the same as the length from
    the first intersection to the start of the cycle.
    reusing the hare pointer for that purpose
    */

    hare = nums[0];
    while (tortoise != hare){
        tortoise = nums[tortoise];
        hare = nums[hare];
    }

    return tortoise;

}