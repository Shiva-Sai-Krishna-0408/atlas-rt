from dotenv import load_dotenv
load_dotenv()
from atlas_rt.agent import app
from atlas_rt.stubs.databases import EMAIL_LOG, PAYMENT_LOG

def print_stream(stream):
    for chunk in stream:
        for node, update in chunk.items():
            if not isinstance(update, dict) or "messages" not in update:
                continue
            message = update["messages"][-1]
            if isinstance(message, tuple):
                print(message)
            else:
                message.pretty_print()

config = {"configurable" : {"thread_id" : "user_1"}}

while True:
    user_input = input("You: ")
    if not user_input or user_input.lower() in {"quit", "exit"}:
        break
    inputs = {"messages": [("user", user_input)]}
    print_stream(app.stream(inputs, config, stream_mode="updates"))

print(EMAIL_LOG)
print(PAYMENT_LOG)