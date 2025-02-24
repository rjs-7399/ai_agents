import os
from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
from langchain_openai import OpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

openai_llm = OpenAI(model="gpt-4o-mini")
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")
