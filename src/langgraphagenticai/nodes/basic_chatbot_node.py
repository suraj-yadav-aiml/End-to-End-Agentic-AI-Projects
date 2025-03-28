from src.langgraphagenticai.state.state import State

class BasicChatBotNode:
    def __init__(self,model):
        self.llm = model
    
    def process(self, state: State):
        messages = state['messages']
        response = self.llm.invoke(
            input = messages
        )

        return {
            'messages': response
        }