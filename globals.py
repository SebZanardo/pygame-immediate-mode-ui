import pygame
import constants as c


pygame.init()

window: pygame.window.Window = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
clock: pygame.time.Clock = pygame.time.Clock()

mouse_pos: pygame.Vector2 = pygame.Vector2(-1, -1)
mouse_clicked: bool = False
mouse_held: bool = False

# Load assets here
FONT = pygame.font.Font("Better VCR 9.0.1.ttf", 16)
