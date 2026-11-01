HANDOFF_WORDS = ["book", "schedule", "change", "cancel",]


class ApointmentAssistant:
    def __init__(self, name, instructions, tool):
        self.name = name
        self.instructions = instructions
        self.tool = tool
        self.history = []

    def respond(self, user_message):
        """Record the user's message, choose a reply, record it, and return it"""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Chose a reply with keyword rules. This is the mock part"""
        text = user_message.lower()
        if self.needs_human(text):
            return (
                " I cannot help with that here. I am passing you on to a human agent."
            )
        if "appointment" in text:
            return self.appointment_reply(user_message)
        if "hello" in text:
            return (
                f"Hello! I am {self.name}. I can check an appointment status for you."
            )
        return (
            " I am not sure how to respond to that. Can you ask about an appointment?"
        )

    def needs_human(self, text):
        """Return True if the message is about something a person might handle"""
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def appointment_reply(self, user_message):
        day = self.tool.find_day(user_message)
        if day is None:
            return "Which day? I can check Monday, Wednesday, or Friday."
        times = self.tool.get_times(day)
        return f"Open times on {day}: {times}."

    def test_count_user_messages(self):
        """Return the number of user messages in the history"""
        count = 0
        for message in self.history:
            if message["role"] == "user":
                count += 1
        return count
