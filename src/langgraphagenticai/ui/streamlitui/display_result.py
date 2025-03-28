import streamlit as st

class DisplayResultStreamlit:
    def __init__(self,usecase,graph,user_message):
        self.usecase= usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase= self.usecase
        graph = self.graph
        user_message = self.user_message
        
        if usecase =="Basic Chatbot":
            for event in graph.stream({'messages':("user",user_message)}):
                for node_name, node_output in event.items():
                    ai_message = node_output['messages'].content
                    with st.chat_message("user"):
                        st.markdown(user_message)
                    with st.chat_message("assistant"):
                        st.markdown(ai_message)
        
        elif usecase=="Chatbot with Tool":
            pass