import pygame
from pygame.locals import QUIT
import sys
from environment import Environment
from agent import Agent
from graph import Graph
from heuristic import IHeuristic, RandomHeuristic
from menu import Button, Menu

pygame.init()
vec = pygame.math.Vector2

HEIGHT = 700
WIDTH = 1500
FPS = 60

FramePerSec = pygame.time.Clock()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Traveling Salesman")

graph = Graph(window)
graph.load_graph("./data/graph_3.csv"
                 )
environment = Environment(window=window, graph=graph)

menu = Menu(window, environment)

run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            break

    window.fill((0, 0, 0))
    environment.update()
    environment.draw()
    menu.draw()
    pygame.display.update()
    FramePerSec.tick(FPS)

pygame.quit()
sys.exit()
