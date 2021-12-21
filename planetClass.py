import pygame
import math
size = (1920, 1080)


class Planet:
  def __init__(self, name, radius, colour, speed, distance, mass, angle, orbitcentrex, orbitcentrey):
    self.y = None
    self.x = None
    self._name = name
    self._radius = radius
    self._colour = colour
    self._speed = speed
    self._distance = distance
    self._angle = angle
    self._centreX = orbitcentrex
    self._centreY = orbitcentrey

  def render(self, screen):
    self.updatePos()
    pygame.draw.circle(screen, MercuryColour, [size[0]/2, size[1]/2], self._distance, 1)
    pygame.draw.circle(screen, self._colour, [self.x, self.y], self._radius)

  def updatePos(self):
    self._angle += self._speed
    xChange = math.sin(self._angle)*self._distance
    yChange = math.cos(self._angle)*self._distance
    self.x = xChange + self._centreX
    self.y = yChange + self._centreY

  def getx(self):
    return (math.sin(self._angle)*self._distance) + self._centreX

  def gety(self):
    return (math.cos(self._angle)*self._distance) + self._centreX

  def speedUp(*planets):
    for planet in planets:
      planet._speed += (0.2*(planet._speed))

  def slowDown(*planets):
    for planet in planets:
      planet._speed -= (0.2*planet._speed)

  def stop(*planets):
    for planet in planets:
      planet._speed -= planet._speed

  def go(*planets):
    for planet in planets:
      planet._speed += planet._speed

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
