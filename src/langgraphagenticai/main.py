import os 
import json 
import streamlit as st 
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI 
from src.langgraphagenticai.LLMs.groqllm import GroqLLM 
from src.langgraphagenticai.graph.graph_builder import GraphBuilder 
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit


def load_langgraph_agenticai_app(): 
    """ 
    """ 

    ui = LoadStreamlitUI()  
    user_input = ui.load_streamlit_ui()  

    if st.sidebar.button("Clear chat"): 
        st.session_state.IsClearChatButtonClicked = True


    if not user_input: 
        st.error("Failed to load the UI") 
        return 
    

    if st.session_state.IsFetchButtonClicked: 
        user_message = st.session_state.timeframe 
    elif st.session_state.IsSDLC: 
        user_message = st.session_state.state
    else: 
        user_message = st.chat_input("Enter your query here")   


    if user_message:  
        try: 
                    
            groq_obj = GroqLLM(user_controls_input = user_input) 

            model = groq_obj.get_llm_model() 
            if not model: 
                st.error("Error: LLM could not be initialized")
                return   
            
            usecase = user_input["selected_usecase"] 
            if not usecase: 
                st.error("Error: Use case not selected")
                return  
            
            try: 
                graph_builder = GraphBuilder(model = model)
                graph = graph_builder.setup_graph(usecase = usecase) 
            except Exception as e: 
                raise ValueError(f"Error while setting up the graph: {e}") 
                return 
            
            display_obj = DisplayResultStreamlit(graph= graph, user_message=user_message, usecase=usecase) 
            display_obj.display_result() 
            

        except Exception as e: 
            raise ValueError(f"Error occured with exception: {e}") 
        

 
         


        
