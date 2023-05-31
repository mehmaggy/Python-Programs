import pygame
pygame.font.init() 
white = (255, 255, 255)
height = 400
width = 400
display_surface = pygame.display.set_mode((height,width ))

image = pygame.image.load(r'ICT360.png')
while True :
    display_surface.fill(white)
    display_surface.blit(image, (70, 80))
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :     
            pygame.quit()
            quit()  
        pygame.display.update() 
