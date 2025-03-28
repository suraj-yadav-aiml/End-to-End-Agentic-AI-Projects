from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatBotNode

from langgraph.graph import START, END, StateGraph

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)
    
    def basic_chatbot_build_graph(self):
        
        self.graph_builder.add_node("chatbot", BasicChatBotNode(self.llm).process)

        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
    
    def chatbot_with_tools_build_graph(self):
        pass

    def setup_graph(self, usecase: str):
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        elif usecase == "Chatbot with Tool":
            self.chatbot_with_tools_build_graph()
        
        return self.graph_builder.compile()
        
