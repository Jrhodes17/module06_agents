# appoint_main.py
# Author: James Rhodes

from appointment_bot import AppointmentHelper
from appointment_tool import AppointmentBook
from ollama_model import OllamaModel

OPEN_TIMES = {
    "monday": "8:00 am and 3:30 pm",
    "wednesday": "12:00 am",
    "friday": "none",
}

INSTRUCTIONS = """You are Larry, an assistant for Bayside Tax Help.
Answer in one short sentence.
The office is at 4121 office street, on the 5th floor.
Bring a photo ID and last year's tax return to your appointment.
Only state facts that appear in these instructions.
If you do not know, say you don't know and offer to pass the client to the front desk."""

appointment_book = AppointmentBook(OPEN_TIMES)
model = OllamaModel("granite4.1:3b")
helper = AppointmentHelper("Larry", INSTRUCTIONS, appointment_book, model)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{helper.name}: {helper.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(helper.history)}")
