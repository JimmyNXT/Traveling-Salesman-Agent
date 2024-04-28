from edge import Edge

class Vertex:
    def __init__(self, id: int, name: str, edges:list[Edge]) -> None:
        self.id = id
        self.name = name
        self.edges = edges