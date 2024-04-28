from vertex import Vertex

class Edge:
    def __init__(self, id:int, vertexA:Vertex, vertexB:Vertex) -> None:
        self.id = id
        self.vertexA = vertexA
        self.vertexB = vertexB