import streamlit as st

from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.llms.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()
    print(user_input)

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return
    
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe 
    else :
        user_message = st.chat_input("Enter your message:")
    

    if user_message:
        try:
            groq = GroqLLM(user_controls_input=user_input)
            groq_llm = groq.get_llm_model()

            if not groq_llm:
                st.error("Error: LLM model could not be initialized.")
                return
            
            usecase = user_input.get('selected_usecase')

            if not usecase:
                st.error("Error: No use case selected.")
                return
            
            graph_builder = GraphBuilder(model=groq_llm)

            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph setup failed - {e}")
                return


        except Exception as e:
                 raise ValueError(f"Error Occurred with Exception : {e}")