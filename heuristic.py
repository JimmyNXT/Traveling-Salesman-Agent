from graph import Graph, Vertex
import random


class IHeuristic:
    def __init__(self, graph:Graph, id:int) -> None:
        self.graph = graph
        self.id = id

    def get_edge_value(self, nodeid:int, visited:List[Vertex]) -> float:
        raise NotImplementedError("This Function has not been implemented")

class RandomHeuristic(IHeuristic):
    def __init__(self, graph: Graph, id: int) -> None:
        super().__init__(graph, id)

    def get_edge_value(self, nodeid: int, visited: List[Vertex]) -> float:
        return random.randrange(0, len(self.graph.vertexes)) 
