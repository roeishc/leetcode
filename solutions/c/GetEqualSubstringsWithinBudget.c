#define max(a, b) a < b ? b : a

int equalSubstring(char* s, char* t, int maxCost) {
    
    int tempCost, maxLen, start, n;
    tempCost = maxLen = start = 0;
    n = strlen(s);

    for (int i = 0; i < n; i++){
        tempCost += abs(s[i] - t[i]);
        while (maxCost < tempCost)
            tempCost -= abs(s[start] - t[start++]);
        maxLen = max(maxLen, i - start + 1);
    }

    return maxLen;

}