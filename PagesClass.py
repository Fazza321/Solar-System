import os

import pygame
from pygame import mixer

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
SunColour = (230, 230, 0)
MercuryColour = (131, 134, 139)
VenusColour = (231, 227, 224)
EarthColour = (0, 0, 255)
MarsColour = (253, 133, 96)
JupiterColour = (217, 199, 176)
SaturnColour = (178, 167, 122)
UranusColour = (143, 161, 171)
NeptuneColour = (108, 139, 183)
PlutoColour = (235, 193, 153)

size = (1920, 1080)
click = mixer.Sound(os.path.join("static", "buttonclick.wav"))
Font = pygame.font.Font(os.path.join("static", "Dosis-ExtraLight.ttf"), 45)
TitleFont = pygame.font.Font(os.path.join("static", "Dosis-ExtraLight.ttf"), 80)

Background = pygame.image.load(os.path.join("static", "Stars.jpg"))
Background = pygame.transform.scale(Background, size)

EarthImage = pygame.image.load(os.path.join("static", "Earth.png"))
EarthImage = pygame.transform.scale(EarthImage, [1200, 1200])
