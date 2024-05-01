from graph import graph
from agent import agent

class Environment:
    def __init__(self, graph:graph, agent:agent) -> None:
        self.graph:graph = graph
        self.agent:agent = agent