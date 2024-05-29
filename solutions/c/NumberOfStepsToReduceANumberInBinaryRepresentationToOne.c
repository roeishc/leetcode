int numSteps(char* s) {
    int len, res, i, consecutiveOnes;
    len = strlen(s);
    res = 0;
    for (i = len - 1; 0 < i; i--){
        if (s[i] == '0')
            res++;
        else{
            consecutiveOnes = 0;
            while (0 <= i && s[i] == '1'){
                consecutiveOnes++;
                i--;
            }
            if (0 < i)
                s[i] = '1';
            res += consecutiveOnes + 1;
            i++;
        }
    }
    return res;
}