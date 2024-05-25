def get_partitions(s: str, wordDict: List[str], start: int, partition: List[str], res: [List[str]]):
    if start == len(s):
        res.append(' '.join(partition))
        return
    for word in wordDict:
        if s[start:].find(word) == 0:   # "word" is the prefix of the string (starting from "start")
            get_partitions(
                s=s,
                wordDict=wordDict,
                start=start + len(word),
                partition=partition + [word],
                res=res
            )


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res: List[str] = []
        get_partitions(
            s=s,
            wordDict=wordDict,
            start=0,
            partition=[],
            res=res
        )
        return res
