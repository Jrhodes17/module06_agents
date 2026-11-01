class AppointmentLookup:
    def __init__(self, schedule):
        self.schedule = schedule

    def find_appointment_id(self, text):
        text_lower = text.lower()
        for day in self.schedule:
            if day in text_lower:
                return day
        return None

    def get_times(self, day):
        if day in self.schedule:
            return self.schedule[day]
        return None

    def find_day(self, text):
        text_lower = text.lower()
        for day in self.schedule:
            if day in text_lower:
                return day
        return None
