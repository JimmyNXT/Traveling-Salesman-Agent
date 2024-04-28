from graph.vertex import Vertex
from heuristic.weighted_heuristic import WeightedHeuristic

class Agent:
    def __init__(self, id: int, heuristics:list[WeightedHeuristic]) -> None:
        self.id:int = id
        self.heuristics:list[WeightedHeuristic] = heuristics
        self.current_vertex:Vertex = None
        self.viseted_vertexes:list[Vertex] = None


