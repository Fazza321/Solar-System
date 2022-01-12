import math

from PagesClass import *

size = (1920, 1080)


class Planet:
    def __init__(
        self,
        name,
        radius,
        colour,
        speed,
        distance,
        mass,
        angle,
        orbiting_planet,
        centre_of_screen,
    ):
        self.y = None
        self.x = None
        self.name = name
        self.radius = radius
        self.colour = colour
        self.speed = speed
        self.distance = distance
        self.angle = angle
        self.orbiting_planet = orbiting_planet
        self.centre_of_screen = centre_of_screen

    def render(self, screen):
        self.updatePos()
        pygame.draw.circle(
            screen, MercuryColour, [self.centre_x(), self.centre_y()], self.distance, 1
        )
        pygame.draw.circle(screen, self.colour, [self.x, self.y], self.radius)

    def updatePos(self):
        self.angle += self.speed
        xChange = math.sin(self.angle) * self.distance
        yChange = math.cos(self.angle) * self.distance
        self.x = xChange + self.centre_x()
        self.y = yChange + self.centre_y()

    def centre_x(self):
        if self.orbiting_planet is not None:
            return self.orbiting_planet.x
        else:
            return self.centre_of_screen[0]

    def centre_y(self):
        if self.orbiting_planet is not None:
            return self.orbiting_planet.y
        else:
            return self.centre_of_screen[1]

    def centre_xa(self):
        return self.x

    def centre_ya(self):
        return self.y

    def getname(self):
        return self.name

    @classmethod
    def speedUp(cls, planets):
        for planet in planets:
            planet.speed += 0.2 * planet.speed

    @classmethod
    def slowDown(cls, planets):
        for planet in planets:
            planet.speed -= 0.2 * planet.speed

    @classmethod
    def stop(cls, planets):
        for planet in planets:
            planet.speed = 0
