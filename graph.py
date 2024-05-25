import csv
from pygame import Vector2, Surface, draw, display
import random

import pygame
from pygame.color import Color

class Vertex:
    def __init__(self, id: int, window:Surface, position:Vector2) -> None:
        self.id:int = id
        self.neighbours:dict[int, float]={}
        self.window:Surface = window
        self.position:Vector2 = position
        self.force:Vector2 = Vector2(0,0)
        self.radius:int = 10
        self.clicked:bool = False
    
    def add_edge(self, vertex_id:int, distance:float):
        self.neighbours.update({vertex_id: distance})
    
    def draw(self, colour: Color):
        mouse_position:Vector2 = Vector2(pygame.mouse.get_pos())

        if mouse_position.distance_to(self.position) <= self.radius:
            if pygame.mouse.get_pressed()[0]  == 1:
                self.clicked = True
            else:
                self.clicked = False
        else:
            if self.clicked and pygame.mouse.get_pressed()[0]  == 0:
                self.clicked = False

        if self.clicked:
            self.position = mouse_position
            self.force = Vector2(0, 0)
        

        draw.circle(self.window, colour, [self.position.x, self.position.y], self.radius)

    def get_position(self):
        return [self.position.x, self.position.y]
    
    def update(self):
        if self.clicked:
            return
        self.position = self.position + self.force
    
    def __repr__(self):
        return "Vertex; " + str(self.id)
    
    # def __str__(self):
    #     return str(self.id)
    
    def __hash__(self):
        return hash(str(self))
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id
        else:
            return False
        

class Graph:
    def __init__(self, window:Surface) -> None:
        self.vertexes:dict[int, Vertex] = {}
        self.window:Surface = window
        w, h = display.get_surface().get_size()
        self.center:Vector2 = Vector2(w/3,h/2)
        self.gravity_constant = 1.1
        self.force_constant = 1000
    
    def add_vertex(self, vertex:Vertex):
        if vertex.id not in self.vertexes:
            self.vertexes.update({vertex.id: vertex})

    def add_edge(self, vertex_a_id:int, vertex_b_id:int, distance:float):
        self.vertexes.get(vertex_a_id).add_edge(vertex_id=vertex_b_id, distance=distance)
        self.vertexes.get(vertex_b_id).add_edge(vertex_id=vertex_a_id, distance=distance)
        
    
    def load_graph(self, path:str):
        with open(path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            graph_data:list[list[float]] = []

            for row in csv_reader:
                line_data:list[float]=[]
                for cell in row:
                    line_data.append(float(cell))
                graph_data.append(line_data) 
            
            row_count = len(graph_data)
            if row_count <= 0:
                raise Exception("Do data in graph")
            
            for row in graph_data:
                col_count = len(row)
                if row_count != col_count:
                    raise Exception("Graph shape miss match")
            
            for i in range(len(graph_data)):
                w, h = display.get_surface().get_size()
                x = random.randint(0, w)
                y = random.randint(0, h)
                self.add_vertex(Vertex(i, self.window, Vector2(x, y)))

            for i in range(len(graph_data)):
                for j in range(len(graph_data[0])):
                    if int(graph_data[i][j]) != 0:
                        self.add_edge(i, j, float(graph_data[i][j]))
            
    def draw(self):
        lines:set[list[int, int]] = []
        for vertex in self.vertexes.values():
            vertex.draw(Color(0, 0, 255))
            for n in vertex.neighbours.keys():
                lines.append((vertex.id, n))
        
        for line in lines:
            draw.line(
                    self.window, 
                    "blue", 
                    self.vertexes.get(line[0]).get_position(),
                    self.vertexes.get(line[1]).get_position())

    def get_neighbours(self, id:int) -> list[int]:
        vertex:Vertex|None = self.vertexes.get(id)
        if vertex:
            return list(vertex.neighbours.keys())

        raise IndexError("Could not find Vertex")
    
    def update(self):
        for vertex in self.vertexes.values():
            force:Vector2 = (vertex.position - self.center) * self.gravity_constant
            vertex.force = -force
        
        for vertexA in self.vertexes.values():
            for vertexB in self.vertexes.values():
                if vertexA.id != vertexB.id:
                    pos:Vector2 = vertexA.position
                    dir:Vector2 = pos - vertexB.position
                    force = Vector2(0, 0)
                    try:
                        force = (dir / (dir.magnitude() * dir.magnitude())) * -self.force_constant
                    except:
                        pass
                    vertexA.force = vertexA.force - force
                    vertexB.force = vertexB.force + force
        
        for vertex in self.vertexes.values():
            edges:dict[int, float]=vertex.neighbours
            for vertex_id in edges.keys():
                
                current_vertex:Vertex|None = self.vertexes.get(vertex_id)
                if current_vertex is None:
                    continue
                
                dir:Vector2 = vertex.position - current_vertex.position

                current_edge:float|None = edges.get(vertex_id)
                if current_edge is None:
                    continue

                try:
                    dir.scale_to_length(current_edge)
                    vertex.force = vertex.force + dir
                except:
                    pass

        for vertex in self.vertexes.values():
            vertex.update()
