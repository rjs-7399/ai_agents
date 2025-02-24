import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_openai import OpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

load_dotenv()

openai_llm = OpenAI(model="gpt-4o-mini")
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")
search_tool = TavilySearchResults(max_result=2)

system_prompt="Act as an AI chatbot who is smart and friendly"

agent=create_react_agent(
    model=groq_llm,
    tools=[search_tool],
    state_modifier=system_prompt
)

query = "Tell me about the trends in crypto markets"
state = {"messages": query}
response = agent.invoke(state)
messages = response.get("messages")
ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
print(ai_messages[-1])
