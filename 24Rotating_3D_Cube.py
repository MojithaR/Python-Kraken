# Rotating_3D_Cube.py

import pygame
import math

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rotating 3D Cube")

# Cube vertices
vertices = [
    [-1, -1, -1],
    [-1, -1,  1],
    [-1,  1, -1],
    [-1,  1,  1],
    [ 1, -1, -1],
    [ 1, -1,  1],
    [ 1,  1, -1],
    [ 1,  1,  1]
]

# Edges connecting the vertices
edges = [
    (0, 1), (1, 3), (3, 2), (2, 0),
    (4, 5), (5, 7), (7, 6), (6, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# Rotation angles
angle_x = angle_y = angle_z = 0

# Rotate vertices
def rotate_x(point, angle):
    x, y, z = point
    y = y * math.cos(angle) - z * math.sin(angle)
    z = y * math.sin(angle) + z * math.cos(angle)
    return [x, y, z]

def rotate_y(point, angle):
    x, y, z = point
    x = x * math.cos(angle) + z * math.sin(angle)
    z = -x * math.sin(angle) + z * math.cos(angle)
    return [x, y, z]

def rotate_z(point, angle):
    x, y, z = point
    x = x * math.cos(angle) - y * math.sin(angle)
    y = x * math.sin(angle) + y * math.cos(angle)
    return [x, y, z]

# Project 3D points to 2D
def project(point):
    fov = 256
    distance = 4
    factor = fov / (distance + point[2])
    x = point[0] * factor + width // 2
    y = -point[1] * factor + height // 2
    return [x, y]

# Main loop
def main():
    global angle_x, angle_y, angle_z
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Rotate and project vertices
        projected_points = []
        for vertex in vertices:
            rotated_x = rotate_x(vertex, angle_x)
            rotated_y = rotate_y(rotated_x, angle_y)
            rotated_z = rotate_z(rotated_y, angle_z)
            projected_points.append(project(rotated_z))

        # Draw edges
        for edge in edges:
            points = [projected_points[edge[0]], projected_points[edge[1]]]
            pygame.draw.line(screen, (255, 255, 255), points[0], points[1], 1)

        # Update rotation angles
        angle_x += 0.01
        angle_y += 0.01
        angle_z += 0.01

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
