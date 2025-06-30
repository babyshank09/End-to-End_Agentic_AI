import os 
from langchain_groq import ChatGroq 
import streamlit as st 


class GroqLLM: 

    def __init__(self, user_controls_input): 
        self.user_controls_input = user_controls_input  
         
    def get_llm_model(self): 
        try:
            groq_api_key = self.user_controls_input["GROQ_API_KEY"] 
            selected_model = self.user_controls_input["selected_groq_model"]  

            if groq_api_key == "" and os.environ["GROQ_API_KEY"] == "":  
                st.error("⚠️ Please enter your Groq API key to proceed!") 

            llm = ChatGroq(model = selected_model, api_key = groq_api_key) 
        
        except Exception as e: 
            raise ValueError(f"Error initializing Groq LLM: {e}") 
        
        return llm 
    
