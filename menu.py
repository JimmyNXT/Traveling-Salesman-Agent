from typing import Callable
import pygame
from pygame import Rect, Surface, Color

class Button():
    def __init__(self, window:Surface, rectangle:Rect, text:str, handleClick:Callable) -> None:
        self.window:Surface = window
        self.color:Color = Color(0, 255, 0)
        self.rectangle:Rect = rectangle
        self.text:str = text
        self.handleClick = handleClick
        self.clicked = False

    def setText(self, text:str):
        self.text = text

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


class Menu():
    def __init__(self, window:Surface) -> None:
        self.window:Surface = window
        self.buttons:list[Button] = []
        pass

    def add_button(self, button:Button):
        self.buttons.append(button)

    def draw(self):
        for button in self.buttons:
            button.draw()



