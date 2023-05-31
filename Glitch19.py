import pygame
import sys
pygame.display.init()
display = pygame.display.set_mode((400, 400))
image = pygame.image.load('ICT360.png')
display.blit(image,(80,100))
pygame.time.wait(1200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()