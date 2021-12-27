import math

import pygame

size = (1920, 1080)

from dataclasses import dataclass


class Planet:
  def __init__(self, name, radius, colour, speed, distance, mass, angle, orbiting_planet, centre_of_screen):
    self.y = None
    self.x = None
    self._name = name
    self._radius = radius
    self._colour = colour
    self._speed = speed
    self._distance = distance
    self._angle = angle
    self._orbiting_planet = orbiting_planet
    self._centre_of_screen = centre_of_screen

  def render(self, screen):
    self.updatePos()
    pygame.draw.circle(screen, MercuryColour, [self.centre_x(), self.centre_y()], self._distance, 1)
    pygame.draw.circle(screen, self._colour, [self.x, self.y], self._radius)

  def updatePos(self):
    self._angle += self._speed
    xChange = math.sin(self._angle)*self._distance
    yChange = math.cos(self._angle)*self._distance
    self.x = xChange + self.centre_x()
    self.y = yChange + self.centre_y()

  def getx(self):
    return (math.sin(self._angle)*self._distance) + self.centre_x()

  def gety(self):
    return (math.cos(self._angle)*self._distance) + self.centre_y()

  def centre_x(self):
    if self._orbiting_planet is not None:
      return self._orbiting_planet.x
    else:
      return self._centre_of_screen[0]

  def centre_y(self):
    if self._orbiting_planet is not None:
      return self._orbiting_planet.y
    else:
      return self._centre_of_screen[1]

  @classmethod
  def speedUp(cls, planets):
    for planet in planets:
      planet._speed += (0.2*(planet._speed))

  @classmethod
  def slowDown(cls, planets):
    for planet in planets:
      planet._speed -= (0.2*planet._speed)

  @classmethod
  def stop(cls, planets):
    for planet in planets:
      planet._speed -= planet._speed

  @classmethod
  def go(cls, planets):
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
