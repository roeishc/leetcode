class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
        list1 = sentence1.split(" ")
        list2 = sentence2.split(" ")

        if len(list1) < len(list2):
            shorter = list1
            longer = list2
        else:
            shorter = list2
            longer = list1

        l = 0   # left pointer
        while l < len(shorter) and longer[l] == shorter[l]:
            l += 1

        r_shorter = len(shorter) - 1    # right shorter & right longer pointers
        r_longer = len(longer) - 1
        while r_shorter >= 0 and r_longer >= 0 and shorter[r_shorter] == longer[r_longer]:
            r_shorter -= 1
            r_longer -= 1

        return l > r_shorter
