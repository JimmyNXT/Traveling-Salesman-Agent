import pygame
from pygame.locals import *
import sys
import csv

class Vertex:
    def __init__(self, id: int, name: str = "") -> None:
        self.id:int = id
        self.edges:list[Edge] = None
    
    def __repr__(self):
        return "Vertex; " + str(self.id)
    
    def __str__(self):
        return "Vertex; " + str(self.id)
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id
        else:
            return False
    
    
    def addEdge(self, edge):
        self.edges.append(edge)
        

class Edge:
    pass
    # def __init__(self, id:int, vertexes:list[Vertex]) -> None:
    #     self.id = id
    #     if len(vertexes) != 2:
    #         raise Exception("The number of vertexes passed in is not 2")
        
    #     self.vertexes:list[Vertex] = vertexes
    
    def __init__(self, id:int):
        self.id = id
        self.vertexes:list[Vertex] = None

    def __repr__(self):
        return "Edge: " + str(self.id)
    
    def __str__(self):
        return "Edge: " + str(self.id)

    def addVertex(self, vertex):
        if len(self.addVertex) >= 2:
            raise Exception("Vertex limit has been reached")
        
        self.vertexes.append(vertex)

class Graph:
    def __init__(self) -> None:
        pass
        self.edges:list[Edge] = None
        self.vertexes:list[Vertex] = None
    
    def load_graph(self, path:str):
        with open(path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            graph_data:list[list[float]] = []

            for row in csv_reader:
                line_data:list[int]=[]
                for cell in row:
                    line_data.append(cell)
                graph_data.append(line_data) 
            
            row_count = len(graph_data)
            if row_count <= 0:
                raise Exception("Do data in graph")
            
            for row in graph_data:
                col_count = len(row)
                if row_count != col_count:
                    raise Exception("Graph shape miss match")
            
            vertex_dict:dict[int, Vertex] = {}
            for i in range(len(graph_data)):
                vertex_dict.update({i: Vertex(i)})
            
            print(vertex_dict)


graph = Graph()
graph.load_graph("C:/Users/jimmynxt/OneDrive/Documents/GitHub/Traveling-Salesman-Agent/data/graph_1.csv")
 
# pygame.init()
# vec = pygame.math.Vector2  # 2 for two dimensional
 
# HEIGHT = 700
# WIDTH = 1500
# FPS = 60
 
# FramePerSec = pygame.time.Clock()
 
# displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Traveling Salesman")

# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
     
#     displaysurface.fill((0,0,0))
 
#     pygame.display.update()
#     FramePerSec.tick(FPS)