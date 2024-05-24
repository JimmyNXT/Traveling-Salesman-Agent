
from pygame import Surface
from graph import Graph, Vertex
from logger import Logger
from weighted_heuristic import WeightedHeuristic

class Agent:
    def __init__(self, 
                 window:Surface, 
                 graph:Graph, 
                 id:int,
                 heuristic_weights:list[WeightedHeuristic],
                 starting_vertex_id: int
                 ) -> None:
        self.window:Surface = window
        self.graph:Graph = graph
        self.id:int = id
        self.weighted_heuristics:list[WeightedHeuristic] = heuristic_weights 
        self.current_vertex_id:int = starting_vertex_id 
        self.viseted_vertexes:list[int] = []
        self.distance_traveled:float = 0
        self.logger = Logger("Agent " + str(self.id))
        self.done = False

    def _check_done(self):
        if (len(self.graph.vertexes.keys()) - len(self.viseted_vertexes)) <= 0:
            self.done = True

    def mutate(self):
        for weighted_heuristic in self.weighted_heuristics:
            weighted_heuristic.mutate()

    def reset(self):
        self.current_vertex_id = 0
        self.viseted_vertexes = []
        self.distance_traveled = 0
        self.done = False

    def update(self):
        if self.done:
            return

        avaliable_vertex_ids:list[int] = self.graph.get_neighbours(self.current_vertex_id)

        vertex_values:dict[int,float] = {}

        if len(avaliable_vertex_ids) <= 0:
            self.done = True
            return

        for vertex_id in avaliable_vertex_ids:
            vertex_values.update({vertex_id: 0})

        for vertex_id in avaliable_vertex_ids:
            vertex_value = 0
            
            for weighted_heuristic in self.weighted_heuristics:
                vertex_value = vertex_value + weighted_heuristic.get_weighted_edge_value(
                        self.current_vertex_id,
                        vertex_id,
                        self.viseted_vertexes[0],
                        self.viseted_vertexes
                        )  

            vertex_values.update({vertex_id: vertex_value})

        next_vertex_id:int = max(zip(vertex_values.values(), vertex_values.keys()))[1]
        
        current_vertex:Vertex|None = self.graph.vertexes.get(self.current_vertex_id)

        if current_vertex is None:
            raise IndexError("Unable to find current vertex in graph")
        

        next_vertex:Vertex|None = self.graph.vertexes.get(next_vertex_id)

        if next_vertex is None:
            raise IndexError("Unable to find next vertex in graph")
        
       

        self.distance_traveled = self.distance_traveled + current_vertex.position.distance_to(next_vertex.position)
        self.viseted_vertexes.insert(0, self.current_vertex_id)
        self.current_vertex_id = next_vertex_id


