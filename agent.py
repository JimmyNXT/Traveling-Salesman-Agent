from csv import QUOTE_ALL
from os import walk

from pygame import Color, Surface
from graph import Graph, Vertex
from logger import Logger
from weighted_heuristic import IHeuristic

class Agent:
    def __init__(self, 
                 window:Surface, 
                 graph:Graph, 
                 id:int,
                 colour: Color,
                 heuristics:list[IHeuristic], 
                 heuristic_weights:dict[int,float],
                 starting_vertex_id: int
                 ) -> None:
        self.window:Surface = window
        self.graph:Graph = graph
        self.id:int = id
        self.colour:Color = colour
        self.heuristics:list[IHeuristic] = heuristics
        self.heuristic_weights:dict[int,float] = heuristic_weights 
        self.current_vertex_id:int = starting_vertex_id 
        self.viseted_vertexes:list[int] = []
        self.distance_traveled:float = 0
        self.logger = Logger("Agent " + str(self.id))
        self.done = False

    def _check_done(self):
        if len(set(self.graph.vertexes) - len(set(self.viseted_vertexes))) == 0:
            self.done = True

    def reset(self):
        self.current_vertex_id = 0
        self.viseted_vertexes = []
        self.distance_traveled = 0
        self.done = False

    def draw(self):
        if self.done:
            return

        vertex_ids:list[int] = self.viseted_vertexes
        vertex_ids.append(self.current_vertex_id)

        for vertex_id in vertex_ids:
            curr_vertex:Vertex|None = self.graph.vertexes.get(vertex_id)
            if curr_vertex:
                curr_vertex.draw(self.colour)

    def update(self):
        if self.done:
            return

        avaliable_vertex_ids:list[int] = self.graph.get_neighbours(self.current_vertex_id)

        vertex_values:dict[int,float] = {}

        if len(avaliable_vertex_ids) <= 0:
            return

        for vertex_id in avaliable_vertex_ids:
            vertex_values.update({vertex_id: 0})

        for vertex_id in avaliable_vertex_ids:
            vertex_value = 0
            
            for heuristic in self.heuristics:
                heuristic_weight:float|None = self.heuristic_weights.get(heuristic.id)
                if not heuristic_weight:
                    raise IndexError("No weight for heuristic with id '" + str(heuristic.id) + ".")
                vertex_value = (
                        vertex_value + 
                        (
                            heuristic.get_edge_value(
                                current_vertex_id = self.current_vertex_id,
                                vertex_id=vertex_id,
                                visited=self.viseted_vertexes) * heuristic_weight
                        ))

            vertex_values.update({vertex_id: vertex_value})

        next_vertex_id:int = max(vertex_values, key=vertex_values.get)

        current_vertex:Vertex|None = self.graph.vertexes.get(self.current_vertex_id)

        if not current_vertex:
            raise IndexError("Unable to find current vertex in graph")

        next_vertex_distance:float|None = current_vertex.neighbours.get(next_vertex_id)

        if not next_vertex_distance:
            raise IndexError("Unable to find next vertex in graph")

        self.distance_traveled = self.distance_traveled + next_vertex_distance
        self.viseted_vertexes.append(self.current_vertex_id)
        self.current_vertex_id = next_vertex_id


