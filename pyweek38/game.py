import pygame
from settings import *


class Game:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(WINDOW_TITLE)

        self.clock = pygame.time.Clock()

        self.running = False
    

    def start(self):
        self.running = True

        while self.running:
            self._draw_background()
            self._process_events()
            self._update_display()
        
        pygame.quit()
        quit()
    

    def _draw_background(self):
        self.window.fill(pygame.Color(255, 255, 255))
    

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    

    def _update_display(self):
        pygame.display.update()
        self.clock.tick(FPS)
