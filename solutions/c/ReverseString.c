void reverseString(char* s, int sSize) {
    char temp = '\0';
    // for (int i = 0; i < sSize / 2; i++){
    for (int i = sSize / 2 - 1; i >= 0; i--){
        temp = s[sSize - 1 - i];
        s[sSize - 1 - i] = s[i];
        s[i] = temp;
    }
}