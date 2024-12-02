import pygame
import sys
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Physics Engine Test")
class Object:
    def __init__(self, x, y, velocity_x=0, velocity_y=0, acceleration_x=0, acceleration_y=0, radius=20):
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.acceleration_x = acceleration_x
        self.acceleration_y = acceleration_y
        self.radius = radius
    def update(self):
        self.velocity_x += self.acceleration_x
        self.velocity_y += self.acceleration_y
        self.x += self.velocity_x
        self.y += self.velocity_y
object1 = Object(200, 300, velocity_x=1, acceleration_y=0.05, radius=30)
object2 = Object(600, 300, velocity_x=-1, acceleration_y=0.05, radius=20)
platform = pygame.Rect(100, 500, 600, 20)
left_wall = pygame.Rect(0, 0, 20, height)
right_wall = pygame.Rect(width - 20, 0, 20, height)
elasticity = 0.8
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    object1.update()
    object2.update()
    if object1.x - object1.radius < left_wall.right or object1.x + object1.radius > right_wall.left:
        object1.velocity_x *= -elasticity
    if object1.y + object1.radius >= platform.top:
        object1.velocity_y *= -elasticity
        object1.y = platform.top - object1.radius
    if object2.x - object2.radius < left_wall.right or object2.x + object2.radius > right_wall.left:
        object2.velocity_x *= -elasticity
    if object2.y + object2.radius >= platform.top:
        object2.velocity_y *= -elasticity
        object2.y = platform.top - object2.radius
    pygame.draw.circle(screen, (255, 0, 0), (int(object1.x), int(object1.y)), object1.radius)
    pygame.draw.circle(screen, (0, 0, 255), (int(object2.x), int(object2.y)), object2.radius)
    pygame.draw.rect(screen, (0, 0, 0), platform)
    pygame.draw.rect(screen, (0, 0, 0), left_wall)
    pygame.draw.rect(screen, (0, 0, 0), right_wall)
    pygame.display.flip()
    pygame.time.Clock().tick(60) 