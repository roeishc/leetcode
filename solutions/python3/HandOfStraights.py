class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False

        freqs = defaultdict(int)
        for card in hand:
            freqs[card] += 1
        freqs = {k: v for k, v in sorted(freqs.items(), key=lambda item: item[0])}

        group: list = []
        freqs_list = [list(item) for item in list(freqs.items())]

        while freqs_list:
            if len(group) == groupSize:
                group = []
            for i, pair in enumerate(freqs_list):
                if len(group) == groupSize:
                    break
                k, v = pair[0], pair[1]
                if 0 < v:
                    group.append(k)
                    freqs_list[i][1] -= 1
                else:
                    freqs_list.pop(i)
                    break
            if len(group) == groupSize:
                for i in range(len(group) - 1):
                    if group[i] != group[i + 1] - 1:
                        return False

        return True