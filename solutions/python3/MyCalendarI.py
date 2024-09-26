class MyCalendar:

    def __init__(self):
        self.booked = []

    def book(self, start: int, end: int) -> bool:
        for cur_start, cur_end in self.booked:
            if (
                cur_start <= start < cur_end            # start in an existing book
                or
                cur_start < end <= cur_end              # end in an existing book
                or
                cur_start <= start and end <= cur_end   # the new book is a subset of an existing book
                or
                start <= cur_start and cur_end <= end   # existing book is a subset of the new book
            ):
                return False
        self.booked.append([start, end])
        return True
        

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)