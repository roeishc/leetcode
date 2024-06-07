class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        words = sentence.split(" ")
        shortest_root: str
        res: str = ""

        for word in words:
            shortest_root = None
            for root in dictionary:
                if word.find(root) == 0 and len(root) < len(word):  # viable root
                    if shortest_root is None or len(root) < len(shortest_root): # shortest root
                        shortest_root = root
            if shortest_root is None:
                res += word + " "
            else:
                res += shortest_root + " "
        
        res = res[:len(res) - 1]    # remove last space
        
        return res
        