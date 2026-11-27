import os

from dotenv import load_dotenv
from tavily import TavilyClient

from scratch_agents.tools.base import tool

load_dotenv()
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def calculator(expression: str) -> float:
    """Calculate mathematical expressions"""
    return eval(expression)

@tool
def search_web(query: str, max_results: int = 5, topic: str = "general", time_range: str | None = None) -> list | str:
    """Search the web for the given query"""
    try:
        response = tavily_client.search(query, max_results=max_results, topic=topic, time_range=time_range)
        return response.get("results")

    except Exception as e:
        return f"Error: Search Failed - {e}"