char* reversePrefix(char* word, char ch) {
    
    char* firstOccurence = strchr(word, ch);
    if (firstOccurence == NULL)
        return word;

    int index = (int)(firstOccurence - word);
    char temp = '\0';
    
    for (int i = 0; i <= index / 2; i++){
        temp = word[index - i];
        word[index - i] = word[i];
        word[i] = temp;
    }

    return word;

}