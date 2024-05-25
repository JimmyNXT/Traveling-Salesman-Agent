import random
import sys
from pygame import Color, Surface, fastevent
import pygame
from pygame.font import Font
from graph import Graph, Vertex
from agent import Agent
from heuristic import (
    AngleDeltaHeuristic,
    DirectionChangeHeuristic,
    DistanceHeuristic,
    HasVisitedHeuristic,
    IHeuristic,
    RandomHeuristic,
)
from weighted_heuristic import WeightedHeuristic


class Environment:
    def __init__(self, window: Surface, graph: Graph) -> None:
        self.font: Font = pygame.font.Font("freesansbold.ttf", 16)
        self.window: Surface = window
        self.graph: Graph = graph
        self.agents: dict[int, Agent] = {}
        self.animate_graph: bool = True
        self.run_agents: bool = False
        self.heuristics: list[IHeuristic] = self.getHeuristics()
        self.base_genes: dict[int, float] = {0: 1, 1: 100, 2: 1, 3: 1, 4: 1}
        self.agent_count: int = 100
        self.reproduction_population: int = 10
        self.populate_agents()
        self.generation:int = 0

    def getHeuristics(self) -> list[IHeuristic]:
        heuristics: list[IHeuristic] = []
        # heuristics.append(RandomHeuristic(self.graph, 0))
        heuristics.append(HasVisitedHeuristic(self.graph, 1))
        heuristics.append(DistanceHeuristic(self.graph, 2))
        heuristics.append(DirectionChangeHeuristic(self.graph, 3))
        heuristics.append(AngleDeltaHeuristic(self.graph, 4))
        # heuristics.append(RandomHeuristic(self.graph, 5))
        # heuristics.append(RandomHeuristic(self.graph, 6))
        # heuristics.append(RandomHeuristic(self.graph, 6))

        return heuristics

    def populate_agents(self):
        self.agents.clear()
        for i in range(self.agent_count):
            weigted_heuristics: list[WeightedHeuristic] = []
            for heuristic in self.heuristics:
                weight = self.base_genes.get(heuristic.id)
                if weight is None:
                    weight = 0

                weight = weight + random.uniform(weight - 10, weight + 10)

                weigted_heuristics.append(WeightedHeuristic(weight, heuristic))

            self.agents.update(
                {i: Agent(self.window, self.graph, i, weigted_heuristics, 0)}
            )

    def agents_Done(self) -> bool:
        done_counter: int = 0
        for agent in self.agents.values():
            if done_counter >= self.reproduction_population:
                return True
            if agent.done:
                done_counter = done_counter + 1
        return False

    def mutate_agents(self):
        for agent in self.agents.values():
            agent.mutate()

    def toggleGraphAnimation(self):
        self.animate_graph = not self.animate_graph

    def toggleRunAgents(self):
        self.run_agents = not self.run_agents
        # self.reset_agents()

    def add_agent(self, agent: Agent):
        self.agents.update({len(self.agents.keys()): agent})

    def reset_agents(self):
        self.populate_agents()
        # for agent in self.agents.values():
        #     agent.reset()

    def propogate(self):
        self.generation = self.generation + 1
        new_agents:dict[int,Agent] = {}
        for i in range(self.reproduction_population):
            new_agent = self.get_fittest_agent()
            if new_agent is None:
                continue
            self.agents.pop(new_agent.id, None)
            new_agent.id = i
            new_agents.update({new_agent.id: new_agent})

        while len(new_agents.keys()) < self.agent_count:
            temp_new_agents:dict[int,Agent] = {}
            for agent_a in new_agents.values():
                if len(new_agents.keys()) >= self.agent_count:
                    break
                for agent_b in new_agents.values():
                    if len(new_agents.keys()) >= self.agent_count:
                        break

                    current_new_agent:Agent = self.breed_agents(agent_a, agent_b)
                    current_new_agent.id = len(new_agents.keys())
                    temp_new_agents.update({current_new_agent.id: current_new_agent})
            new_agents.update(temp_new_agents)

        self.agents = {}

        for agent in list(new_agents.values()):
            self.add_agent(agent)

        self.mutate_agents()
        self.reset_agents()

    def breed_agents(self, agent_a:Agent, agent_b:Agent) -> Agent:
        weigted_heuristics: list[WeightedHeuristic] = []
        for heuristic in self.heuristics:
            gene_pool:dict[int,float] = {}
            random_num = random.uniform(0, 1)
            if random_num >= 0.5:
                gene_pool = agent_a.get_genes()
            else:
                gene_pool = agent_b.get_genes()

            weight = gene_pool.get(heuristic.id)

            if weight is None:
                weight = 0

            weigted_heuristics.append(WeightedHeuristic(weight, heuristic))

        return Agent(self.window, self.graph, 0, weigted_heuristics, 0)

        

    def update(self):
        if self.agents_Done():
            self.propogate()

        if self.animate_graph:
            self.graph.update()

        if self.run_agents:
            for agent in self.agents.values():
                agent.update()

        
    def get_fittest_agent(self) -> Agent | None:
        if len(self.agents.keys()) <= 0:
            return None

        agents: list[Agent] = list(self.agents.values())
        agents.sort()

        return agents[0]

    def print_list(self, text: list[str], x: int, y: int):
        lable: list[Surface] = []

        for line in text:
            lable.append(self.font.render(line, True, Color(255, 255, 255)))

        for line in range(len(lable)):
            self.window.blit(
                lable[line], (x, (y + (line * self.font.get_height()) + 10 * line))
            )

    def print_stats(self):
        env_stats: list[str] = [
            "Graph Physics: " + str(self.animate_graph),
            "Agents Running: " + str(self.run_agents),
            "Agent Count: " + str(len(self.agents.keys())),
        ]

        self.print_list(env_stats, 10, 10)

        fittest_agent = self.get_fittest_agent()

        agent_stats: list[str] = []

        if fittest_agent is not None:
            agent_stats.append("Generation: " + str(self.generation))
            agent_stats.append("Fittest Agent")
            agent_stats.append("---------------------")
            agent_stats.append("ID: " + str(fittest_agent.id))
            agent_stats.append("Distance: " + str(fittest_agent.distance_traveled))
            agent_stats.append(
                "Visited Count: " + str(len(fittest_agent.viseted_vertexes))
            )
            agent_stats.append("Best Path : " + fittest_agent.get_path_string())

        window_height: int = self.window.get_height()
        self.print_list(agent_stats, 10, window_height - (20 + (22 * len(agent_stats))))

    def draw_best_path(self):
        fittest_agent:Agent|None = self.get_fittest_agent()

        if fittest_agent is None:
            return
        
        path: list[int] = fittest_agent.viseted_vertexes.copy()
        if len(path) <= 0:
            return


        current_vertex_id = 0
        previous_vertex_id = -1


        while len(path) >= 0:
            try:
                current_vertex_id = path.pop(0)
            except:
                break

            current_vertex:Vertex|None = self.graph.vertexes.get(current_vertex_id)
            if current_vertex is None:
                continue

            current_vertex.draw(Color(0, 255, 0))

            previous_vertex:Vertex|None = self.graph.vertexes.get(previous_vertex_id)
            if previous_vertex is None:
                previous_vertex_id = current_vertex_id
                continue

            pygame.draw.line(
                    self.window, 
                    Color(0, 255, 0), 
                    current_vertex.get_position(),
                    previous_vertex.get_position())

            previous_vertex_id = current_vertex_id
            



    def draw(self):
        self.graph.draw()
        self.print_stats()
        self.draw_best_path()

        # for agent in self.agents.values():
        #     agent.draw()
