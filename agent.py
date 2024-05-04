from os import walk

from pygame import Surface
from graph import Graph, Vertex
from weighted_heuristic import IHeuristic

class Agent:
    def __init__(self, 
                 window:Surface, 
                 graph:Graph, 
                 id:int,
                 heuristics:list[IHeuristic], 
                 heuristic_weights:dict[int,float],
                 starting_vertex_id: int
                 ) -> None:
        self.window:Surface = window
        self.graph:Graph = graph
        self.id:int = id
        self.heuristics:list[IHeuristic] = heuristics
        self.heuristic_weights:dict[int,float] = heuristic_weights 
        self.current_vertex_id:int = starting_vertex_id 
        self.viseted_vertexes:list[Vertex] = []

    def draw(self):
        pass

    def update(self):
        self.draw()


