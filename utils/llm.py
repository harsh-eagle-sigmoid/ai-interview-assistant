import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

@st.cache_resource
def load_llm():
    return ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama-3.1-8b-instant",
        temperature=0.3
    )
