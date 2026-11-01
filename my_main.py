from my_assistant import ApointmentAssistant
from my_tool import AppointmentLookup

SCHEDULE = {
    "monday": ["9:00", "10:00", "11:00"],
    "wednesday": ["13:00", "14:00"],
    "friday": ["15:00", "16:00"],
}

tool = AppointmentLookup(SCHEDULE)
bot = ApointmentAssistant("Robin", "Be friendly.", tool)

print("Type a messsage, or type quit to stop.")
user_message = input("You: ")
while user_message.lower() != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")
