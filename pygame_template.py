#!/usr/bin/env python3
from enum import Enum
from datetime import datetime
import pygame
from pygame.locals import *

class App:
    windowWidth = 1152
    windowHeight = 768
    FPS = 35

    #Color Definitions
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    #Set the background color
    BACKGROUND = BLACK

    def __init__(self):
        """ App object initialization function, here you set variables default values"""
        self._running = True
        self._display_surf = None
        self.image = None
        self.frame_per_sec = None

    def on_init(self):
        """Game initialisation function, here you load scenes, images, sounds, etc."""
        pygame.init()
        pygame.font.init()

        #If font is not installed, use another one
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)

        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        self.frame_per_sec = pygame.time.Clock()

        #Set the window caption
        pygame.display.set_caption("Template for a pygame application")

        #Load Images
        self.image = pygame.image.load("images/pygame.png").convert_alpha()

    def on_event(self, event):
        """Function designed to hanlde events such as user input (keyboard, mouse, etc"""
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            pass
        elif event.type == pygame.KEYUP:
            pass
        elif event.type == pygame.MOUSEBUTTONUP:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
        elif event.type == pygame.MOUSEBUTTONUP:
            pass

    def on_loop(self):
        """Function to specify the game logic"""
        pass

    def on_render(self):
        """Function specialized for surface rendering only"""

        #Fill Backrgound color
        self._display_surf.fill(self.BACKGROUND)

        center_screen = (self.windowWidth//2, self.windowHeight//2)

        #Draw pygame image
        img = self.image
        rect = img.get_rect()
        rect.center = center_screen
        self._display_surf.blit(self.image, rect)

        #Draw pygame version
        version = 'Version : ' + str(pygame.version.ver)
        text_surface = self.myfont.render(version, False, self.WHITE)
        text_size = self.myfont.size(version)
        text_position = center_screen[0] - text_size[0]//2, center_screen[1] + 30
        self._display_surf.blit(text_surface, text_position)

        #Display update instruction
        pygame.display.flip()

    def on_cleanup(self):
        """Function to handle app destruction"""
        pygame.quit()

    def on_execute(self):
        """Main Execute function and main loop, calls on_init, on_event, on_loop, on_logic  """
        #Init application
        if self.on_init() == False:
            self._running = False

        #Main Loop
        while (self._running):
            #Handle Events
            for event in pygame.event.get():
                self.on_event(event)

            #Game Logic
            self.on_loop()

            #Render code
            self.on_render()

            self.frame_per_sec.tick(self.FPS)
        self.on_cleanup()


if __name__ == "__main__":
    """Program entry function"""
    theApp = App()
    theApp.on_execute()
