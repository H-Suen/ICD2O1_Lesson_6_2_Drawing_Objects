import pygame

# Initialize the game engine
pygame.init()

# ---------------------------
# Set window settings (size and name) 
WIDTH = 700
HEIGHT = 375
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Basketball Game")
# ---------------------------

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

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
    screen.fill((0, 0, 0))  # always the first drawing command

    # Drawing Court

        # Border 
    pygame.draw.rect(screen, (255, 0, 0), [0, 0, 700, 375], 5)

        # Middle and logo
    pygame.draw.line(screen, (255, 0, 0), [350, 0], [350, 375], 5)
    pygame.draw.circle(screen, (0, 0, 0), [350, 188], 50)
    pygame.draw.arc(screen, (255, 0, 0), [300, 138, 100, 100], 3.57792, 2.26893, 5)
    pygame.draw.polygon(screen, (255, 0, 0), [[319, 151], [353, 163], [363, 170], [369, 180], 
    [370, 187], [365, 193], [355, 200], [347, 204], [340, 205], [346, 194], [330, 190], [320, 193], 
    [312, 200], [306, 207]], 7)
    pygame.draw.line(screen,(0, 0, 0), [307, 197], [319, 156], 9)
    pygame.draw.arc(screen, (255, 0, 0), [344, 167, 10, 10], 2.87979, 6.02139, 75)

        # 3 point line (right side)
    pygame.draw.line(screen, (255, 0, 0), [665, 27], [700, 27], 5)
    pygame.draw.line(screen, (255, 0, 0), [665, 345], [700, 345], 7)
    pygame.draw.arc(screen, (255, 0, 0), [525, 25, 325, 325], 1.5708, 4.71239, 5)

        # Free throw line (right side)
    pygame.draw.circle(screen, (255, 0, 0), [575, 188], 50, 5)
    pygame.draw.line(screen, (255, 0, 0), [575, 140], [700, 140], 5)
    pygame.draw.line(screen, (255, 0, 0), [575, 235], [700, 235], 5)
    pygame.draw.line(screen, (255, 0, 0), [575, 235], [575, 140], 5)

        # 3 point line (left side)
    pygame.draw.line(screen, (255, 0, 0), [0, 27], [35, 27], 5)
    pygame.draw.line(screen, (255, 0, 0), [0, 345], [35, 345], 7)
    pygame.draw.arc(screen, (255, 0, 0), [-140, 25, 325, 325], 4.71239, 1.5708, 5)

        # Free throw line (left side)
    pygame.draw.circle(screen, (255, 0, 0), [132, 188], 50, 5)
    pygame.draw.line(screen, (255, 0, 0), [0, 140], [125, 140], 5)
    pygame.draw.line(screen, (255, 0, 0), [0, 235], [125, 235], 5)
    pygame.draw.line(screen, (255, 0, 0), [133, 140], [133, 235], 5)

        # Basketball ball
    pygame.draw.circle(screen, (180, 86, 53), [225, 300], 25)
    pygame.draw.line(screen, (0, 0, 0), [225, 275], [225, 325], 2)
    pygame.draw.line(screen, (0, 0, 0), [200, 300], [250, 300], 2)
    pygame.draw.arc(screen, (0, 0, 0), [235, 280, 34, 40], 2.18166, 4.10952, 2)
    pygame.draw.arc(screen, (0, 0, 0), [183, 280, 34, 40], 5.22325, 1.059931, 2)



    # Must be the last two lines of the game loop
    pygame.display.flip()
    clock.tick(30)
    # ---------------------------

pygame.quit()
