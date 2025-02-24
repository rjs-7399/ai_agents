import os
from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
from langchain_openai import OpenAI
from langchain_community.tools.tavily_search import TavilySearchResults