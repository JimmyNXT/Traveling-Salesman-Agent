from graph import Vertex
from weighted_heuristic import IHeuristic

class Agent:
    def __init__(self, id: int, heuristics:list[IHeuristic]) -> None:
        self.id:int = id
        self.heuristics:list[IHeuristic] = heuristics
        self.current_vertex:Vertex = None
        self.viseted_vertexes:list[Vertex] = None


