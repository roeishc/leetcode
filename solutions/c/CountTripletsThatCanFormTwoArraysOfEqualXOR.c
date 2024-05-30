int countTriplets(int* arr, int arrSize) {

    int count = 0;
    int* prefixXor;
    assert(prefixXor = (int*)malloc(sizeof(int) * (arrSize + 1)));

    prefixXor[0] = 0;
    for (int i = 1; i < arrSize + 1; i++) {
        prefixXor[i] = arr[i - 1];
        prefixXor[i] ^= prefixXor[i - 1];
    }

    for (int start = 0; start < arrSize + 1; start++) {
        for (int end = start + 1; end < arrSize + 1; end++) {
            if (prefixXor[start] == prefixXor[end])
                count += end - start - 1;
        }
    }

    free(prefixXor);

    return count;

}