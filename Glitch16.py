import pygame
pygame.font.init()
height=500
width=500
screen = pygame.display.set_mode([height,width])
pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
