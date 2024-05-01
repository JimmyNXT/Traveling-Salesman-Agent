import pygame
from pygame.locals import *
import sys
from graph import Graph

pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional
 
HEIGHT = 700
WIDTH = 1500
FPS = 60
 
FramePerSec = pygame.time.Clock()
 
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Traveling Salesman")

graph = Graph(window)
graph.load_graph("C:/Users/jimmynxt/OneDrive/Documents/GitHub/Traveling-Salesman-Agent/data/graph_1.csv")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
     
    window.fill((0,0,0))
    
    graph.update()
    graph.draw()
    pygame.display.update()
    FramePerSec.tick(FPS)