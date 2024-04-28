from edge import Edge
from vertex import Vertex

class graph:
    def __init__(self, edges:list[Edge], vertexes:list[Vertex]) -> None:
        self.edges = edges
        self.vertexes = vertexes