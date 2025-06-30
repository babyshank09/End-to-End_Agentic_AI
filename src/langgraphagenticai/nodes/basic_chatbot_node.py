from src.langgraphagenticai.state.state import State 


class BasicChatbotNode: 
    """
    Basic chatbot logic implementation.
    """
    
    def __init__(self, model):  
        self.llm = model 


    def process(self, state: State) -> dict:  
        """ 
        processes the input state and generates a response
        """
        response = self.llm.invoke(state["messages"])
        return {"messages": [response]} 
    


