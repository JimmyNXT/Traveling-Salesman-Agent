from os import walk
from pygame import Surface
from graph import Graph
from agent import Agent


class Environment:
    def __init__(self, window:Surface, graph:Graph) -> None:
        self.window:Surface = window
        self.graph:Graph = graph
        self.agents:dict[int, Agent] = {}
        self.animate_graph:bool = True
        self.run_agents:bool = False

    def setShouldAnimateGraph(self, shouldAnimateGraph:bool):
        self.animate_graph = shouldAnimateGraph

    def add_agent(self, agent:Agent):
        self.agents.update({len(self.agents.keys()): agent})

    def reset_agents(self):
        for agent in self.agents.values():
            agent.reset()

    def update(self):
        if self.animate_graph:
            self.graph.update()
        
        if self.run_agents:
            for agent in self.agents.values():
                agent.update()

    def draw(self):
        self.graph.draw()

        for agent in self.agents.values():
            agent.draw()
