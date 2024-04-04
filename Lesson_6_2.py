import pygame
import math 

# Initialize the game engine
pygame.init()

# ---------------------------
# Set window settings (size and name) 
WIDTH = 700
HEIGHT = 500
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("My game")
# ---------------------------

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
font = pygame.font.SysFont('Arial', 25, False, True)
text = font.render('Welcome to my Game', True, (0, 0, 0))
# ---------------------------

# --------------- Main program loop ---------------
running = True
while running:
    # ----- EVENT HANDLING -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ----- GAME STATE UPDATES -----
    # All game math and comparisons happen here

    # ----- DRAWING -----
    screen.fill((255, 255, 255))  # always the first drawing command 

    # pygame.draw.line(screen, (0, 0, 255), [0,0], [700, 0], 300)

    # pygame.draw.line(screen, (255, 0, 0), [0,500], [700, 500], 300)

    # pygame.draw.rect(screen, (135, 206, 235), [0, 0, 700, 170])

    # pygame.draw.rect(screen, (255, 183, 206), [0, 335, 700, 170])

    # pygame.draw.ellipse(screen, (0, 0, 255), [0, 0, 250, 100], 3)

    # pygame.draw.arc(screen, (255, 255, 0), [200, 150, 150, 150], 0.523599, 5.75959, 100)
    # pygame.draw.circle(screen, (0, 0, 0), [300 , 180], 15, 70)

    screen.blit(text, [300, 100])

    # Must be the last two lines of the game loop
    pygame.display.flip()
    clock.tick(30)
    # ---------------------------

pygame.quit()
