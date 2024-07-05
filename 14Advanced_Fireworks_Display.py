# Advanced_Fireworks_Display.py

import pygame
import random
import math

# Initialize pygame
pygame.init()

# Define screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Advanced Fireworks Display")

# Define colors
BLACK = (0, 0, 0)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (255, 192, 203), (75, 0, 130)]

# Firework class
class Firework:
    def __init__(self):
        self.x = random.randint(100, width - 100)
        self.y = height
        self.y_velocity = random.uniform(-10, -14)
        self.exploded = False
        self.particles = []
        self.color = random.choice(colors)
        self.trail = []

    def update(self):
        if not self.exploded:
            self.y += self.y_velocity
            self.y_velocity += 0.15  # Gravity effect
            self.trail.append((self.x, self.y, self.color))
            if self.y_velocity >= 0:  # Firework explodes when it starts falling down
                self.explode()
        else:
            for particle in self.particles:
                particle.update()

    def draw(self):
        if not self.exploded:
            pygame.draw.circle(screen, self.color, (self.x, int(self.y)), 3)
            for t in self.trail:
                pygame.draw.circle(screen, t[2], (t[0], int(t[1])), 2)
        else:
            for particle in self.particles:
                particle.draw()

    def explode(self):
        self.exploded = True
        pattern = random.choice(['circle', 'star', 'burst'])
        if pattern == 'circle':
            self.create_circle_pattern()
        elif pattern == 'star':
            self.create_star_pattern()
        elif pattern == 'burst':
            self.create_burst_pattern()

    def create_circle_pattern(self):
        for _ in range(100):
            self.particles.append(Particle(self.x, self.y, self.color, 'circle'))

    def create_star_pattern(self):
        for _ in range(50):
            self.particles.append(Particle(self.x, self.y, self.color, 'star'))

    def create_burst_pattern(self):
        for _ in range(200):
            self.particles.append(Particle(self.x, self.y, self.color, 'burst'))

# Particle class
class Particle:
    def __init__(self, x, y, color, pattern):
        self.x = x
        self.y = y
        self.color = color
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(2, 5)
        self.life = 100
        self.pattern = pattern
        self.size = 2
        self.gravity = 0.02

    def update(self):
        self.life -= 1
        if self.pattern == 'circle':
            self.x += self.speed * math.cos(self.angle)
            self.y += self.speed * math.sin(self.angle)
        elif self.pattern == 'star':
            self.x += self.speed * math.cos(self.angle) * (1 + math.sin(6 * self.angle))
            self.y += self.speed * math.sin(self.angle) * (1 + math.sin(6 * self.angle))
        elif self.pattern == 'burst':
            self.x += self.speed * math.cos(self.angle) * random.uniform(0.5, 1.5)
            self.y += self.speed * math.sin(self.angle) * random.uniform(0.5, 1.5)
        self.y += self.gravity * self.life  # Apply gravity over time
        self.speed *= 0.95  # Friction effect
        self.size = max(0, self.size - 0.05)  # Gradually reduce size

    def draw(self):
        if self.life > 0:
            alpha = max(0, int(255 * (self.life / 100)))
            color_with_alpha = self.color + (alpha,)
            pygame.draw.circle(screen, color_with_alpha, (int(self.x), int(self.y)), int(self.size))

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

        if random.randint(0, 10) == 0:  # Probability to launch a new firework
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
