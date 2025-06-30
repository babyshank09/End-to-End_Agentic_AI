from langgraph.graph import StateGraph, START, END 
from langgraph.prebuilt import tools_condition, ToolNode 
from langchain_core.prompts import ChatPromptTemplate   
import datetime  
from src.langgraphagenticai.state.state import State 
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode



class GraphBuilder: 

    def __init__(self, model): 
        self.llm = model  
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self): 
        """
        Builds a basic chatbot graph using Langgraph.
        """  
        basic_chatbot_node = BasicChatbotNode(model = self.llm)
        self.graph_builder.add_node("basic_chatbot", basic_chatbot_node.process) 
        self.graph_builder.add_edge(START, "basic_chatbot")
        self.graph_builder.add_edge("basic_chatbot", END) 

    def setup_graph(self, usecase: str): 
        """
        Sets up the graph based on the use case.
        """
        if usecase == "Basic Chatbot":  
            self.basic_chatbot_build_graph()  
        return self.graph_builder.compile() 
    
        


 


