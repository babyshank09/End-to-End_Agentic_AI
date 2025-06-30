import json 
import streamlit as st  
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage  
from src.langgraphagenticai.state.state import State


class DisplayResultStreamlit:
    def __init__(self, graph, user_message, usecase): 
        self.graph = graph 
        self.user_message = user_message 
        self.usecase = usecase    
 

    def display_result(self):     
       
        if "chat_history" not in st.session_state or st.session_state.IsClearChatButtonClicked == True:
            st.session_state["chat_history"] = []  
            st.session_state.IsClearChatButtonClicked = False 
        
        a= type(HumanMessage(content="hi")) 
        b= type(AIMessage(content="hi there"))
        for msg in st.session_state["chat_history"]: 
            if type(msg)==a:  
                st.chat_message("user").write(msg.content) 
            if type(msg)==b and msg.content is not '':  
                st.chat_message("assistant").write(msg.content)  

        if self.usecase == "Basic Chatbot": 
            st.chat_message("user").write(self.user_message) 
            st.session_state["chat_history"].append(HumanMessage(content= self.user_message)) 

            answer = self.graph.invoke({"messages": st.session_state.chat_history})
            st.chat_message("assistant").write(answer["messages"][-1].content)
            st.session_state["chat_history"].append(AIMessage(content=answer["messages"][-1].content)) 
    

    