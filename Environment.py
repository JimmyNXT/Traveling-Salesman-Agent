from os import walk
from pygame import Color, Rect, Surface
import pygame
from pygame.font import Font
from graph import Graph
from agent import Agent
from heuristic import AngleDeltaHeuristic, DirectionChangeHeuristic, DistanceHeuristic, HasVisitedHeuristic, IHeuristic, RandomHeuristic
from weighted_heuristic import WeightedHeuristic


class Environment:
    def __init__(self, window:Surface, graph:Graph) -> None:
        self.font:Font = pygame.font.Font('freesansbold.ttf', 16)
        self.window:Surface = window
        self.graph:Graph = graph
        self.agents:dict[int, Agent] = {}
        self.animate_graph:bool = True
        self.run_agents:bool = False
        self.heuristics:list[IHeuristic] = self.getHeuristics()
        self.base_genes:dict[int, float] = {0:1,
                                            1:1,
                                            2:1,
                                            3:1,
                                            4:1}
        self.agent_count = 10
        self.populate_agents()

    def getHeuristics(self) -> list[IHeuristic]:
        heuristics:list[IHeuristic] = []
        heuristics.append(RandomHeuristic(self.graph, 0))        
        heuristics.append(HasVisitedHeuristic(self.graph, 1))
        heuristics.append(DistanceHeuristic(self.graph, 2))
        heuristics.append(DirectionChangeHeuristic(self.graph, 3))
        heuristics.append(AngleDeltaHeuristic(self.graph, 4))
        # heuristics.append(RandomHeuristic(self.graph, 5))
        # heuristics.append(RandomHeuristic(self.graph, 6))
        # heuristics.append(RandomHeuristic(self.graph, 6))

        return heuristics

    def populate_agents(self):
        for i in range(self.agent_count):
            weigted_heuristics:list[WeightedHeuristic] = []
            for heuristic in self.heuristics:
                weight = self.base_genes.get(heuristic.id)
                if weight is None:
                    weight = 0
                weigted_heuristics.append(WeightedHeuristic(weight, heuristic))
            
            self.agents.update({i: Agent(self.window, self.graph, i, weigted_heuristics, 0)})

    def agents_Done(self) -> bool:
        for agent in self.agents.values():
            if not agent.done:
                return False
        return True

    def mutate_agents(self):
        for agent in self.agents.values():
            agent.mutate()
            
    def toggleGraphAnimation(self):
        self.animate_graph = not self.animate_graph

    def toggleRunAgents(self):
        self.run_agents = not self.run_agents
        self.reset_agents()

    def add_agent(self, agent:Agent):
        self.agents.update({len(self.agents.keys()): agent})

    def reset_agents(self):
        for agent in self.agents.values():
            agent.reset()

    def propogate(self):
        pass

    def update(self):
        if self.animate_graph:
            self.graph.update()
        
        if self.run_agents:
            for agent in self.agents.values():
                agent.update()

        if self.agents_Done():
            self.propogate()

    def print_stats(self):
        position = 10, 10
        text:list[str] = [
                "Test 123", "Test 321", "Hello"]

        lable:list[Surface] = []

        for line in text:
            lable.append(self.font.render(line, True, Color(255, 255, 255)))

        for line in range(len(lable)):
            self.window.blit( lable[line], (10, (10+(line*self.font.get_height())+15*line)))


    def draw(self):
        self.graph.draw()
        self.print_stats()

        # for agent in self.agents.values():
        #     agent.draw()
