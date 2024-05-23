from os import walk
from pygame import Surface
from graph import Graph
from agent import Agent

class Environment:
    def __init__(self, window:Surface, graph:Graph, agents:dict[int, Agent]) -> None:
        self.window:Surface = window
        self.graph:Graph = graph
        self.agents:dict[int, Agent] = agents

    def update(self):
        self.graph.update()

        for agent in self.agents.values():
            agent.update()

    def draw(self):
        self.graph.draw()

        for agent in self.agents.values():
            agent.draw()
