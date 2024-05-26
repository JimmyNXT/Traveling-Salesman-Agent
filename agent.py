
from typing import List
from pygame import Surface, Vector2
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
        self.should_continue = True

    def __lt__(self, obj):
        if self.done and not obj.done:
            return True
        if not self.done and obj.done:
            return False

        if not self.done and not obj.done:
            s_list = list(dict.fromkeys(self.viseted_vertexes))
            o_list = list(dict.fromkeys(obj.viseted_vertexes))
            s_len = len(s_list)
            o_len = len(o_list)

            if s_len != o_len:
                return (s_len > o_len)


        if self.distance_traveled != obj.distance_traveled:
            return ((self.distance_traveled) < (obj.distance_traveled))
        else:
            return (len(self.viseted_vertexes) < len(obj.viseted_vertexes))
  
    def __gt__(self, obj):
        return ((self.distance_traveled) > (obj.distance_traveled)) 
  
    def __le__(self, obj): 
        return ((self.distance_traveled) <= (obj.distance_traveled)) 
  
    def __ge__(self, obj): 
        return ((self.distance_traveled) >= (obj.distance_traveled)) 
  
    def __eq__(self, obj): 
        return (self.distance_traveled == obj.distance_traveled)

    def __repr__(self):
        return ", ".join([
                "ID: " + str(self.id),
                "Distance: " + str(self.distance_traveled),
                "Done: " + str(self.done)
                ]) + "\n"

    def _check_done(self):
        if len(self.viseted_vertexes) > len(self.graph.vertexes.keys()) * 3:
            self.should_continue = False
            return

        graph_vertexes_copy = self.graph.vertexes.copy()

        for vertex_id in self.viseted_vertexes:
            try:
                graph_vertexes_copy.pop(vertex_id)
            except:
                pass

        if len(graph_vertexes_copy.keys()) <= 0:
            self.should_continue = False
            self.done = True

    def mutate(self):
        for weighted_heuristic in self.weighted_heuristics:
            weighted_heuristic.mutate()

    def reset(self):
        self.current_vertex_id = 0
        self.viseted_vertexes = []
        self.distance_traveled = 0
        self.done = False
        self.should_continue = True

    def get_path_string(self):
        visited_rev:list[int] = self.viseted_vertexes.copy()
        visited_rev.reverse()
        return "->".join(map(str,visited_rev))
    
    def get_genes(self) -> dict[int,float]:
        gene_dict:dict[int, float] = {}

        for weighted_heuristic in self.weighted_heuristics:
            gene_dict.update({weighted_heuristic.heuristic.id: weighted_heuristic.weight})

        return gene_dict


    def update(self):
        if self.done:
            return

        if not self.should_continue:
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

            previous_vertex_id = None

            if len(self.viseted_vertexes) >= 1:
                previous_vertex_id = self.viseted_vertexes[0]

            
            for weighted_heuristic in self.weighted_heuristics:
                vertex_value = vertex_value + weighted_heuristic.get_weighted_edge_value(
                        self.current_vertex_id,
                        vertex_id,
                        previous_vertex_id,
                        self.viseted_vertexes
                        )  

            vertex_values.update({vertex_id: vertex_value})

        # print(vertex_values)

        next_vertex_id:int = max(zip(vertex_values.values(), vertex_values.keys()))[1]
        
        current_vertex:Vertex|None = self.graph.vertexes.get(self.current_vertex_id)

        if current_vertex is None:
            raise IndexError("Unable to find current vertex in graph")
        

        next_vertex:Vertex|None = self.graph.vertexes.get(next_vertex_id)

        if next_vertex is None:
            raise IndexError("Unable to find next vertex in graph")
        
       
        neighbour_distance = current_vertex.neighbours.get(next_vertex_id)

        if neighbour_distance is None:
            neighbour_distance = float('inf')

        self.distance_traveled =self.distance_traveled + neighbour_distance
        self.viseted_vertexes.insert(0, self.current_vertex_id)
        self.current_vertex_id = next_vertex_id
        self._check_done()


