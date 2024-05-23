from os import walk
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
graph.load_graph("./data/graph_1.csv")

heuristics: list[IHeuristic] = []
heuristics.append(RandomHeuristic(graph, 0))

environment = Environment(window=window, graph=graph)
environment.add_agent(
    Agent(window, graph, 0, pygame.Color(255, 0, 0), heuristics, {0: 1}, 0)
)

menu = Menu(window)


def handle_toggle_grapg_animation():
    environment.animate_graph = not environment.animate_graph


animate_graph_button = Button(
    window,
    pygame.Rect(1050, 10, 400, 50),
    "Toggle Graph Animation",
    handle_toggle_grapg_animation,
)
menu.add_button(animate_graph_button)


# c:/users/jimmynxt/onedrive/documents/github/traveling-salesman-agent

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
