# Game_of_Life.py

import pygame
import numpy as np

# Initialize pygame
pygame.init()

# Define screen dimensions
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Conway's Game of Life")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define grid dimensions
rows, cols = 50, 50
cell_width = width // cols
cell_height = height // rows

# Initialize grid with random state
grid = np.random.choice([0, 1], size=(rows, cols))

def draw_grid(surface, grid):
    for r in range(rows):
        for c in range(cols):
            color = WHITE if grid[r, c] == 1 else BLACK
            pygame.draw.rect(surface, color, (c * cell_width, r * cell_height, cell_width - 1, cell_height - 1))

def update_grid(grid):
    new_grid = np.copy(grid)
    for r in range(rows):
        for c in range(cols):
            state = grid[r, c]
            neighbors = np.sum(grid[r-1:r+2, c-1:c+2]) - state
            if state == 0 and neighbors == 3:
                new_grid[r, c] = 1
            elif state == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[r, c] = 0
    return new_grid

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    draw_grid(screen, grid)
    pygame.display.flip()

    grid = update_grid(grid)
    clock.tick(10)  # Control the speed of the simulation

pygame.quit()
