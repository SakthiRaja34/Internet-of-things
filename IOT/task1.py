import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("audio1.mp3")

def notify():
    pygame.mixer.music.play()

for i in range(3):
    print("Event detected!")
    notify()
    time.sleep(3)