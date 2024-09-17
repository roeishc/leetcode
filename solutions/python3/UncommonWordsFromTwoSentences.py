class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        s1_count = Counter(s1.split())
        s2_count = Counter(s2.split())
        total = s1_count + s2_count
        return [word for word, count in total.items() if count == 1]
