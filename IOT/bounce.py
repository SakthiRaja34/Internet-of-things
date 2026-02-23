import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600,400)) #window creation
pygame.display.set_caption("bouncing ball")

rect=pygame.Rect(400,200,100,100)  #X,Y,width,height

#c0lor
BLACK=(0,0,0)
RED=(255,0,0)

#ball setup
x,y = 100, 100
speed_x, speed_y = 3,2

running = True
clock=pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False

#move ball
    x+=speed_x
    y+=speed_y

#bounce on edges
    if x<=0 or x>=600-20:
         speed_x= -speed_x
    if y<=0 or y>=400-20:
         speed_y= -speed_y

#draw everything
    screen.fill(BLACK) #fill surface black 

    pygame.draw.circle(screen,RED,(x,y),20) #draw rectangle
    pygame.display.flip() 

    clock.tick(60) #frames in 60 sec

pygame.quit()
sys.exit()
