# Colorful_Circles.py

import pygame
import random
import math

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Colorful Circles Animation")

# Colors
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (255, 192, 203), (75, 0, 130)]

# Circle class
class Circle:
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.radius = random.randint(10, 50)
        self.color = random.choice(colors)
        self.growing = True

    def update(self):
        if self.growing:
            self.radius += 1
            if self.radius > 100:
                self.growing = False
        else:
            self.radius -= 1
            if self.radius < 10:
                self.growing = True

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Main loop
def main():
    clock = pygame.time.Clock()
    circles = [Circle() for _ in range(10)]

    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for circle in circles:
            circle.update()
            circle.draw()

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
