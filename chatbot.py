HANDOFF_WORDS = ["address", "payment", "card", "shipping", "human"]


class SupportChatbot:
    def __init__(self, name, instructions, order_tool):
        self.name = name
        self.instructions = instructions
        self.order_tool = order_tool
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
        if "order" in text:
            return self.order_reply(user_message)
        if "hello" in text:
            return f"Hello! I am {self.name}. I can check an order status for you."
        return " I am not sure how to respond to that. Can you ask about an order?"

    def needs_human(self, text):
        """Return True if the message is about something a person might handle"""
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def order_reply(self, user_message):
        order_id = self.order_tool.find_order_id(user_message)
        if order_id is None:
            return (
                "Which order are you asking about? Please send an order ID like A100."
            )
        status = self.order_tool.find_status(order_id)
        return f"Order {order_id} is {status}."

    def test_count_user_messages(self):
        """Return the number of user messages in the history"""
        count = 0
        for message in self.history:
            if message["role"] == "user":
                count += 1
        return count
