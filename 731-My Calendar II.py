class MyCalendarTwo:

    def __init__(self):
        self.overlap = []
        self.calendar = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i, j in self.overlap:
            if start < j and i < end:
                return False
        for i, j in self.calendar:
            if start < j and i < end:
                self.overlap.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True
