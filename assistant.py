from langgraph.graph import StateGraph, START, END
from utils.AgentState import AgentState
from agents.summarisation_agent import Summariser
from services.web_search import search
from database.chroma import get_from_chroma, add_to_chroma
from langchain_core.messages import HumanMessage, AIMessage, FunctionMessage
from export.export import export

class Assistant:

    def __init__(self):
        self.conversation_history = []
        self.summariser = Summariser()
        self.__initilize()

    def __search_node(self, state: AgentState) -> AgentState:
        """ Task for later: Add missing doc string to every function"""
        query = state["messages"][-1].content[0]["query"] # type: ignore
        search_result = search(query)
        self.conversation_history.append(
            FunctionMessage(
                name="search",
                content=[{"result": search_result}]
            )
        )

        return AgentState(messages=self.conversation_history) 

    def __summary_node(self, state: AgentState) -> AgentState:
        query = state["messages"][-2].content[0]["query"] # type: ignore
        result = state["messages"][-1].content[0]["result"] # type: ignore
        summary = self.summariser.summarise(result)
        add_to_chroma(query=query, result=summary)
        self.conversation_history.append(
            AIMessage(
                    content=[{"response": summary}]
                )
            )
        return AgentState(messages=self.conversation_history)

    def __chroma_node(self, state: AgentState) -> AgentState:
        query = state["messages"][-1].content[0]["query"] # type: ignore
        chroma_result = get_from_chroma(query=query)
        if chroma_result:
            self.conversation_history.append(
                AIMessage(
                    content=[{"response": chroma_result}]
                    )
                )
            return AgentState(messages=self.conversation_history) 
        else:
            return state
        
    def __show_response(self, state: AgentState) -> None:
        state["messages"][-1].content[0]["response"] # type: ignore

    def __decideFlow(self, state: AgentState) -> bool:
        latest_message = state["messages"][-1]
        if latest_message and isinstance(latest_message, AIMessage):
            return True
        return False
    
    def __initilize(self):
        graph = StateGraph(AgentState)

        graph.add_node("search", self.__search_node)
        graph.add_node("summarise", self.__summary_node)
        graph.add_node("chroma", self.__chroma_node)
        graph.add_node("show_results", self.__show_response)

        graph.add_edge(START, "chroma")

        graph.add_conditional_edges(
            "chroma",
            self.__decideFlow,
            {
                True: "show_results",
                False: "search"
            }
        )

        graph.add_edge("search", "summarise")
        graph.add_edge("summarise", "show_results")
        graph.add_edge("show_results", END)
        self.app = graph.compile()
    
    def ask(self, query: str) -> dict | None:
        self.conversation_history.append(HumanMessage(content=[{"query": query}]))
        result =  self.app.invoke(AgentState(messages=self.conversation_history))
        return result["messages"][-1].content[0]["response"]
    
    def export(self, filename=""):
        export(filename=filename, chat=self.conversation_history)
