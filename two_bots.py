from chatbot import SupportChatbot
from order_tool import OrderLookup
from stock_tool import StockLookup

order_tool = OrderLookup({"A100": "shipped", "A101": "processing"})
stock_tool = StockLookup({"Widget": 19.99, "Gadget": 29})

Brenard = SupportChatbot(
    "Brenard", "You are cheerful and brief.", order_tool, stock_tool
)
Mackey = SupportChatbot(
    "Mackey", "You are formal and detailed.", order_tool, stock_tool
)

Brenard.respond("Hello!")
Brenard.respond("Where is order A100?")
Mackey.respond("Hello!")

print(Brenard.name, len(Brenard.history))
print(Mackey.name, len(Mackey.history))
print(Brenard.history[1]["content"])
print(Mackey.history[1]["content"])
print(Brenard.instructions)
print(Mackey.instructions)
