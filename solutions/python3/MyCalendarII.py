class MyCalendarTwo:

    def __init__(self):
        self.non_overlapping = []
        self.overlapping = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlapping:
            if not (e <= start or end <= s):    # overlapping with existing overlapping events
                return False
        
        for s, e in self.non_overlapping:
            if not (e <= start or end <= s):
                self.overlapping.append(
                    (max(s, start), min(e, end))
                )
        
        self.non_overlapping.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)