import os
from typing import Literal
from tavily import TavilyClient
from deepagents import create_deep_agent
from langchain.chat_models import init_chat_model

tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool = False,
):
    """Run a web search"""
    return tavily_client.search(
        query,
        max_results=max_results,
        include_raw_content=include_raw_content,
        topic=topic,
    )

# System prompt to steer the agent to be an expert researcher
research_instructions = """You are an expert researcher. Your job is to conduct thorough research and then write a polished report.

You have access to an internet search tool as your primary means of gathering information.

## `internet_search`

Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.
"""


model = init_chat_model(
    model="gpt-4o",
    model_provider="openai",
    api_key=os.environ["OPENAI_API_KEY"],
    base_url=os.environ["OPENAI_API_BASE"]
)

agent = create_deep_agent(
    model=model,
    tools=[internet_search],
    system_prompt=research_instructions
)

result = agent.invoke({"messages": [{"role": "user", "content": "What is langgraph?"}]})

# Print the agent's response
print(result["messages"][-1].content)

"""
(HelloAgent) ➜  HelloAgent git:(main) ✗ python langchain_deep_agent/search_agent.py                  
LangGraph, developed by LangChain, is an open-source AI framework designed to build, deploy, and manage complex generative AI agent workflows. It emphasizes graph-based workflows and state management, making it ideal for applications that require sophisticated logic and memory persistence. LangGraph allows for the development of long-running, stateful AI agents, providing features for scalability and control, making it suitable for production environments.
"""