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

SunImage = pygame.image.load(os.path.join("static", "Sun.png"))
SunImage = pygame.transform.scale(SunImage, [1400, 1400])

MercuryImage = pygame.image.load(os.path.join("static", "Mercury.png"))
MercuryImage = pygame.transform.scale(MercuryImage, [1200, 1200])

VenusImage = pygame.image.load(os.path.join("static", "Venus.png"))
VenusImage = pygame.transform.scale(VenusImage, [1200, 1200])

EarthImage = pygame.image.load(os.path.join("static", "Earth.png"))
EarthImage = pygame.transform.scale(EarthImage, [1200, 1200])

MoonImage = pygame.image.load(os.path.join("static", "Moon.png"))
MoonImage = pygame.transform.scale(MoonImage, [1200, 1200])

MarsImage = pygame.image.load(os.path.join("static", "Mars.png"))
MarsImage = pygame.transform.scale(MarsImage, [1200, 1200])

JupiterImage = pygame.image.load(os.path.join("static", "Jupiter.png"))
JupiterImage = pygame.transform.scale(JupiterImage, [1200, 1200])

SaturnImage = pygame.image.load(os.path.join("static", "Saturn.png"))
SaturnImage = pygame.transform.scale(SaturnImage, [2500, 1400])

UranusImage = pygame.image.load(os.path.join("static", "Uranus.png"))
UranusImage = pygame.transform.scale(UranusImage, [1200, 1200])

NeptuneImage = pygame.image.load(os.path.join("static", "Neptune.png"))
NeptuneImage = pygame.transform.scale(NeptuneImage, [1200, 1200])

PlutoImage = pygame.image.load(os.path.join("static", "Pluto.png"))
PlutoImage = pygame.transform.scale(PlutoImage, [1200, 1200])
