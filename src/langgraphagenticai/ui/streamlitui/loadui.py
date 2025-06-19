import os 
from datetime import date 
import streamlit as st 
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage 
from src.langgraphagenticai.ui.uiconfigfile import Config


class LoadStreamlitUI:  
    def __init__(self): 
        self.config = Config() 
        self.user_controls = {}  

    
    def load_streamlit_ui(self): 
        st.set_page_config(page_title="🤖" + self.config.get_page_title(), layout="wide") 
        st.header("🤖" + self.config.get_page_title())
        st.session_state.timeframe = ""
        st.session_state.IsFetchButtonClicked = False
        st.session_state.IsSDLC = False


        with st.sidebar:  
            llm_options = self.config.get_llm_options()   

            self.user_controls["selected_llm"] = st.selectbox("Select Model", llm_options) 

            if self.user_controls["selected_llm"] == "Groq":   
                groq_model_options = self.config.get_groq_model_options()
                st.user_controls["selected_groq_model"] = st.selectbox("Select Use Case", groq_model_options)   

                self.user_controls["GROQ_API_KEY"] = st.text_input("Enter the Groq API key")  
                if not self.user_controls["GROQ_API_KEY"]: 
                    st.warning("⚠️ Please enter your Groq API key to proceed!")  

            usecase_options = self.config.get_usecase_options() 
            st.user_controls["selected_usecase"] = st.selectbox("Choose the Use Case", usecase_options)   

            



