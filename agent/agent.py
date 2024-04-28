from graph.vertex import Vertex

class Agent:
    def __init__(self) -> None:
        self.id:int = id
        self.current_vertex:Vertex = None
        self.viseted_vertexes:list[Vertex] = None
