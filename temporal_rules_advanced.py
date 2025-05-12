# temporal_rules_advanced.py

class AllenTemporalLogic:
    def __init__(self, event_A, event_B):
        """
        Initialize with two events. Each event is represented by a tuple (start_time, end_time).
        """
        self.A_start, self.A_end = event_A
        self.B_start, self.B_end = event_B

    def before(self):
        """Check if event A ends before event B starts."""
        return self.A_end < self.B_start

    def meets(self):
        """Check if event A ends when event B starts."""
        return self.A_end == self.B_start

    def overlaps(self):
        """Check if event A overlaps event B."""
        return (self.A_start < self.B_start) and (self.A_end > self.B_start)

    def starts(self):
        """Check if event A starts exactly when event B starts and ends before event B."""
        return (self.A_start == self.B_start) and (self.A_end < self.B_end)

    def during(self):
        """Check if event A happens during event B."""
        return (self.A_start > self.B_start) and (self.A_end < self.B_end)

    def finishes(self):
        """Check if event A starts before event B and ends exactly when event B ends."""
        return (self.A_start < self.B_start) and (self.A_end == self.B_end)

    def equals(self):
        """Check if event A and event B are equal."""
        return (self.A_start == self.B_start) and (self.A_end == self.B_end)

# Example usage:
if __name__ == "__main__":
    event_A = (100, 120)
    event_B = (120, 150)
    allen = AllenTemporalLogic(event_A, event_B)

    print(f"A before B: {allen.before()}")
    print(f"A meets B: {allen.meets()}")
    print(f"A overlaps B: {allen.overlaps()}")
    print(f"A starts B: {allen.starts()}")
    print(f"A during B: {allen.during()}")
    print(f"A finishes B: {allen.finishes()}")
    print(f"A equals B: {allen.equals()}")

# python temporal_rules_advanced.py

