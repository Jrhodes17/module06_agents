from appointment_bot import AppointmentHelper
from appointment_tool import AppointmentBook
from mock_model import MockModel
from my_assistant import ApointmentAssistant
from my_tool import AppointmentLookup


def make_bot():
    schedule = {
        "monday": ["9:00", "10:00", "11:00"],
        "wednesday": ["13:00", "14:00"],
        "friday": ["15:00", "16:00"],
    }
    return ApointmentAssistant("Robin", "Be friendly.", AppointmentLookup(schedule))


def test_tool_finds_known_day():
    tool = AppointmentLookup({"monday": ["9:00", "10:00"]})
    assert tool.find_day("I want to book an appointment on Monday") == "monday"


def test_missing_day_ask_for_one():
    bot = make_bot()
    assert "Which day?" in bot.respond("Where is my appointment?")


def test_booking_goes_to_human():
    bot = make_bot()
    assert "human" in bot.respond("Please book an appointment for me")


def test_history_records_messages():
    bot = make_bot()
    bot.respond("hello")
    assert len(bot.history) == 2
    assert bot.history[0]["role"] == "user"
    assert bot.history[1]["role"] == "assistant"


class SilentModel:
    """A model that never has an answer. It stands in for Ollama being switched off."""

    def reply(self, instructions, history):
        return None


def make_helper():
    """Build a fresh helper with its own tool for each test."""
    book = AppointmentBook({"monday": "8:00 am and 3:30 pm", "friday": "none"})
    return AppointmentHelper("Larry", "Be clear.", book, MockModel())


def test_unknown_request_gets_a_safe_reply():
    book = AppointmentBook({"monday": "9:00 am and 2:30 pm"})
    helper = AppointmentHelper("Robin", "Be clear.", book, SilentModel())
    assert "try again" in helper.respond("What is your favorite color?")


def test_other_messages_go_to_the_model():
    helper = make_helper()
    assert helper.respond("hello") == "Hello! How can I help you today?"
