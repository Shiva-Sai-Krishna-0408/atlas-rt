from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage, SystemMessage
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END, START
from langgraph.prebuilt import ToolNode
from langchain_openai import ChatOpenAI
from atlas_rt.tools import tools

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

model = ChatOpenAI(model='gpt-4o-mini').bind_tools(tools)

def model_call(state: AgentState) -> AgentState:
  system_prompt = SystemMessage(content="You are a Travel Agent and your job is to help plan a vacation based on the inputs given by the user."
  )

  response = model.invoke([system_prompt] + state["messages"])
  return {"messages":[response]}

def should_continue(state: AgentState):
  messages = state["messages"]
  last_message = messages[-1]
  if not last_message.tool_calls:
    return "end"
  else:
    return "continue"

graph = StateGraph(AgentState)
graph.add_node("travel_agent", model_call)

tool_node = ToolNode(tools=tools)
graph.add_node("tools",tool_node)

graph.add_edge(START,"travel_agent")
graph.add_conditional_edges(
    "travel_agent",
    should_continue,
    {
        "continue":"tools",
        "end":END   
        
    }
    
    )

graph.add_edge("tools","travel_agent")

app = graph.compile()

