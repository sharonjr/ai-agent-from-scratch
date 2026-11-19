import os
from tavily import TavilyClient
from dotenv import load_dotenv
from mcp.server.mcpserver import MCPServer

load_dotenv()
tavily_client = TavilyClient(os.getenv("TAVILY_API_KEY"))

server = MCPServer("custom-tavily-search")

@server.tool()
def search_web(query: str, max_results: int = 5) -> str:
    """
    Search the Web using Tavily API.

    Args:
        query: Search query string
        max_results: Maximum number of results to return (default: 5)

    Returns:
        Search results as formatted string
    """
    try:
        response = tavily_client.search(
            query,
            max_results=max_results,
        )
        results = response.get("results", [])
        return "\n\n".join(
            f"Title: {r['title']}\nURL: {r['url']}\nContent: {r['content']}"
            for r in results
        )
    except Exception as e:
        return f"Error searching web: {str(e)}"
    
if __name__ == "__main__":
    server.run(transport="stdio")

