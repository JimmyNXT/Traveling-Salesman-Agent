from typing import Callable
import pygame
from pygame import Rect, Surface, Color
from pygame.font import Font

from environment import Environment

class Button():
    def __init__(self, window:Surface, rectangle:Rect, text:str, handleClick:Callable) -> None:
        self.font:Font = pygame.font.Font('freesansbold.ttf', 32)
        self.window:Surface = window
        self.color:Color = Color(0, 255, 0)
        self.rectangle:Rect = rectangle
        self.text:Surface = self.font.render(text, True, Color(0, 0, 0))
        self.text_rectangle:Rect = self.text.get_rect()
        self.handleClick = handleClick
        self.clicked = False

        self.text_rectangle.center = (self.rectangle.center)

    def draw(self):
        mouse_position = pygame.mouse.get_pos()

        if self.rectangle.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0]  == 1:
                self.color = Color(255, 0, 0)
                if not self.clicked:
                    self.clicked = True
                    self.handleClick()
            else:
                self.color = Color(0, 255, 0)
                if self.clicked:
                    self.clicked = False

        pygame.draw.rect(self.window, self.color, self.rectangle)
        self.window.blit(self.text, self.text_rectangle)


class Menu():
    def __init__(self, window:Surface, environment:Environment) -> None:
        self.window:Surface = window
        self.environment:Environment = environment
        self.buttons:list[Button] = []



        self.buttons.append(Button(
                window,
                pygame.Rect(1050, 10, 400, 50),
                "Toggle Graph Animation",
                self.environment.toggleGraphAnimation,
            ))

    def draw(self):
        for button in self.buttons:
            button.draw()



