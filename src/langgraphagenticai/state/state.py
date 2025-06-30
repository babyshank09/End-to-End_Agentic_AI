from typing import TypedDict, Annotated 
from langgraph.graph.message import add_messages, AnyMessage 
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


class State(TypedDict): 
    """ 
    Represents the structure of the state in the graph
    """ 
    messages: Annotated[list[AnyMessage], add_messages]   

