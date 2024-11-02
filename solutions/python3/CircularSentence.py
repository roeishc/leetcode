class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        words = sentence.split(" ")
        
        if len(words) == 1:
            if words[0][0] == words[0][-1]:
                return True
            return False

        if words[0][0] != words[-1][-1]:
            return False
        
        for i in range(1, len(words)):
            if words[i - 1][-1] != words[i][0]:
                return False
        
        return True
