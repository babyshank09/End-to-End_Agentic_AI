import os 
from datetime import date 
import streamlit as st 
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage 
from src.langgraphagenticai.ui.uiconfigfile import Config


class LoadStreamlitUI:  
    def __init__(self): 
        self.config = Config() 
        self.user_controls = {}   


    def initialize_requirements(self): 
        return {
            "current_step": "requirements", 
            "requirements": "", 
            "user_stories": "", 
            "po_feedback": "",
            "generated_code": "", 
            "review_feedback": "", 
            "decision": None
        }
    

    def render_requirements(self):  
        st.markdown("## Requirements Submition")
        st.session_state.requirements= st.text_area("Enter your requirements", height=200, key="req_input") 

        if st.button("Submit Requirements", key= "submit_req"): 
            st.session_state["current_state"] = "generate_user_stories" 
            st.session_state.IsSDLC = True

    
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
                self.user_controls["selected_groq_model"] = st.selectbox("Select Use Case", groq_model_options)   

                self.user_controls["GROQ_API_KEY"] = st.text_input("Enter the Groq API key")  
                if not self.user_controls["GROQ_API_KEY"]: 
                    st.warning("⚠️ Please enter your Groq API key to proceed!")  

            usecase_options = self.config.get_usecase_options() 
            self.user_controls["selected_usecase"] = st.selectbox("Choose the Use Case", usecase_options)    


            if "state" not in st.session_state: 
                st.session_state.state = self.initialize_requirements() 
            self.render_requirements()
            

        return self.user_controls