from dotenv import load_dotenv
load_dotenv()
from atlas_rt.agent import app

def print_stream(stream):
  for s in stream:
    message = s["messages"][-1]
    if isinstance(message, tuple):
      print(message)
    else:
      message.pretty_print()

while True:
    user_input = input("You: ")
    if not user_input or user_input.lower() in {"quit", "exit"}:
        break
    inputs = {"messages": [("user", user_input)]}
    print_stream(app.stream(inputs, stream_mode="values"))