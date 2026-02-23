import pygame
import sys

pygame.init()
print(pygame.version.ver)
screen = pygame.display.set_mode((400,300)) #window creation
pygame.display.set_caption("my window")

rect=pygame.Rect(200,100,100,100)  #X,Y,width,height

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
    screen.fill((255,0,0)) #fill surface black 
    pygame.draw.rect(screen,(0,255,0),rect) #draw rectangle
    pygame.display.update() #
pygame.quit()
sys.exit()
