import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("audio.song.mp3")
pygame.mixer.music.play()

time.sleep(5)
pygame.mixer.music.pause()
print("paused")

time.sleep(2)
pygame.mixer.music.unpause()
print("resumed")

time.sleep(5)
pygame.mixer.music.stop()
print("stopped")