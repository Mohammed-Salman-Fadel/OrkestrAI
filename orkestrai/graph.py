from langchain.graphs import StateGraph, Node
from orkestrai.agents.scraper_agent import make_scraper_agent
from orkestrai.agents.parser_agent import make_parser_agent
from orkestrai.agents.analyzer_agent import make_analyzer_agent
from orkestrai.agents.writer_agent import make_writer_agent

def build_graph():
    graph = LangGraph()
    # Nodes
    graph.add_node(Node("scrape", make_scraper_agent()))
    graph.add_node(Node("parse", make_parser_agent()))
    graph.add_node(Node("analyze", make_analyzer_agent()))
    graph.add_node(Node("write", make_writer_agent()))
    # Edges
    graph.add_edge("scrape", "parse", output_key="raw_data", input_key="html")
    graph.add_edge("parse", "analyze", output_key="structured_data", input_key="data")
    graph.add_edge("analyze", "write", output_key="insights", input_key="analysis")
    return graph
