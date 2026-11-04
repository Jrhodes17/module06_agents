# Author: James Rhodes

from chatbot import SupportChatbot
from ollama_model import OllamaModel
from order_tool import OrderLookup
from stock_tool import StockLookup

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = (
    "You are Brenard, a support assistant for Bayside Outfitters. "
    "Answer in one short sentence. "
    "Store hours are 10 am to 7 pm everyday. "
    "Returns are accepted within 30 days with a receipt. "
    "Shipping takes 3 to 5 business days. "
    "Sale items cannot be returned. "
    "Only state facts that appear in these instructions. "
    "If you do not know, say you don't know and offer to pass to a human agent."
)


ORDERS = {
    "A100": "shipped",
    "A101": "processing",
    "A102": "delivered",
}

STOCK = {
    "rain jacket": 12,
    "day pack": 0,
    "trail hat": 5,
}

order_tool = OrderLookup(ORDERS)
stock_tool = StockLookup(STOCK)
model = OllamaModel(MODEL_NAME)
bot = SupportChatbot("Brenard", INSTRUCTIONS, order_tool, stock_tool, model)

print("Type a messsage, or type quit to stop.")
user_message = input("You: ")
while user_message.lower() != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")
