# Import libraries
import numpy as np
import pygame 
import sys 
import math

# Global Variables
SQUARE_SIZE = 100
WIDTH = 8 
HEIGHT = 8
RADIUS = int(SQUARE_SIZE/2 - 5)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH*SQUARE_SIZE, HEIGHT*SQUARE_SIZE))

def draw_board():
    # Draw the board
    for c in range(WIDTH):
        for r in range(HEIGHT):
            pygame.draw.rect(screen, BLUE, (c*SQUARE_SIZE, r*SQUARE_SIZE,SQUARE_SIZE, SQUARE_SIZE))
            if (c+r)%2 == 0:
                pygame.draw.circle(screen, BLACK, (
