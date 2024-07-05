# Fireworks_Display.py

import pygame
import random
import math

# Initialize pygame
pygame.init()

# Define screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fireworks Display")

# Define colors
BLACK = (0, 0, 0)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (255, 192, 203), (75, 0, 130)]

# Firework class
class Firework:
    def __init__(self):
        self.x = random.randint(100, width - 100)
        self.y = height
        self.y_velocity = random.uniform(-8, -12)
        self.exploded = False
        self.particles = []

    def update(self):
        if not self.exploded:
            self.y += self.y_velocity
            self.y_velocity += 0.1  # Gravity effect
            if self.y_velocity >= 0:  # Firework explodes when it starts falling down
                self.explode()
        else:
            for particle in self.particles:
                particle.update()

    def draw(self):
        if not self.exploded:
            pygame.draw.circle(screen, random.choice(colors), (self.x, int(self.y)), 3)
        else:
            for particle in self.particles:
                particle.draw()

    def explode(self):
        self.exploded = True
        for _ in range(100):
            self.particles.append(Particle(self.x, self.y, random.choice(colors)))

# Particle class
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(2, 5)
        self.life = 100

    def update(self):
        self.life -= 1
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        self.speed *= 0.98  # Friction effect

    def draw(self):
        if self.life > 0:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 2)

# Main loop
def main():
    clock = pygame.time.Clock()
    fireworks = []

    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if random.randint(0, 20) == 0:  # Probability to launch a new firework
            fireworks.append(Firework())

        for firework in fireworks[:]:
            firework.update()
            firework.draw()
            if firework.exploded and all(particle.life <= 0 for particle in firework.particles):
                fireworks.remove(firework)

        pygame.display.flip()
        clock.tick(30)  # Control the frame rate

    pygame.quit()

if __name__ == "__main__":
    main()
