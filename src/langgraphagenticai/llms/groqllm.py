import os
import streamlit as st
from langchain_groq import ChatGroq
from typing import Dict, Optional

class GroqLLM:
    """A class to handle the initialization of the Groq LLM model."""
    
    def __init__(self, user_controls_input: Dict[str, str]) -> None:
        """Initializes the GroqLLM class with user input."""
        self.user_controls_input = user_controls_input
        self.llm: Optional[ChatGroq] = None  

    def get_llm_model(self) -> ChatGroq:
        """Returns an instance of the ChatGroq model with the specified parameters.

        Raises:
            ValueError: If API key is missing or an error occurs during initialization.

        Returns:
            ChatGroq: The initialized ChatGroq model instance.
        """
        try:
            groq_api_key = self.user_controls_input.get('GROQ_API_KEY') or os.getenv("GROQ_API_KEY")
            selected_groq_model = self.user_controls_input.get('selected_groq_model')

            if not groq_api_key:
                st.error("Please enter the Groq API KEY.")
                raise ValueError("Groq API key is missing.")

            if not selected_groq_model:
                raise ValueError("No model selected. Please provide a valid model name.")

            # Create and store the LLM instance
            if self.llm is None:
                self.llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model)

            return self.llm

        except Exception as e:
            raise ValueError(f"Error occurred: {e}")
