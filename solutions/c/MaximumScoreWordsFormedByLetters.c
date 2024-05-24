#define NUM_OF_LETTERS 26
#define max(a, b) a < b ? b : a

int maxScoreWords(char** words, int wordsSize, char* letters, int lettersSize, int* score, int scoreSize) {
    int freq[NUM_OF_LETTERS] = {0}; // frequency array of letters

    for (int i = 0; i < lettersSize; i++)
        freq[letters[i] - 'a']++;
    
    int maxScore = 0;
    int subsetLetters[NUM_OF_LETTERS] = {0};
    int numOfSubsets = 1 << wordsSize;
    int L = 0;
    for (int mask = 0; mask < numOfSubsets; mask++){
        memset(subsetLetters, 0, sizeof(subsetLetters));
        for (int i = 0; i < wordsSize; i++){
            if (0 < (mask & (1 << i))){
                L = strlen(words[i]);
                for (int j = 0; j < L; j++)
                    subsetLetters[words[i][j] - 'a']++;
            }
        }
        maxScore = max(maxScore, subsetScore(subsetLetters, NUM_OF_LETTERS, score, scoreSize, freq, NUM_OF_LETTERS));
    }
    return maxScore;
}

int subsetScore(int* subsetLetters, int subsetLettersSize, int* score, int scoreSize, int* freq, int freqSize){
    int totalScore = 0;
    for (int c = 0; c < NUM_OF_LETTERS; c++){
        totalScore += subsetLetters[c] * score[c];
        if (freq[c] < subsetLetters[c])
            return 0;
    }
    return totalScore;
}