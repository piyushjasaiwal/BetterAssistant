import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

def search(content: str) -> str:
    """Searches the web using tavily search API for the given content"""
    # return "some random string"
    tavily_api_key = os.getenv("tavily_api_key")
    tavily_client = TavilyClient(api_key=tavily_api_key)
    response = tavily_client.search(content, max_results=5)
    results = response["results"]
    search_result_string = ""

    for i in range(len(results)):
        # print("==============================================================")
        # print(f"{i+1} result is:")
        # print(results[i]["content"])
        # print("==============================================================")
        search_result_string = "\n".join([result["content"] for result in results])

    return search_result_string

# result = search("What is milky way")
# result = search.invoke("What is milky way")
# print(result)