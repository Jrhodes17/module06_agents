# appoint_tool.py
# Author: James Rhodes


class AppointmentBook:
    """A tool to look up available appointment times by day."""

    def __init__(self, open_times):
        """Store the dictionary of open times."""
        self.open_times = open_times

    def find_day(self, user_message):
        """Search the user message for a day of the week present in the schedule."""
        text = user_message.lower()
        for day in self.open_times:
            if day in text:
                return day
        return None

    def times_for(self, day):
        """Return the available times string for a given day."""
        return self.open_times.get(day)
