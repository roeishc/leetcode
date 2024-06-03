int appendCharacters(char* s, char* t) {
    int sLen, i, j;
    sLen = strlen(s);
    i = j = 0;
    for (; i < sLen; i++){
        if (s[i] == t[j])
            j++;
    }
    return strlen(t) - j;
}