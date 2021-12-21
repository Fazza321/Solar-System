import pygame
from planetClass import *
from pygame import mixer
import time
import random

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
size = (1920, 1080)
click = mixer.Sound("buttonclick.wav")

def Instructions():
    done = False
    Instructions = pygame.display.set_mode(size)
    pygame.display.set_caption("Solar System")

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                done = True
            Mouse = pygame.mouse.get_pos()
            print(Mouse)
            if event.type == pygame.MOUSEBUTTONDOWN and 30 < Mouse[0] < 150 and 180 < Mouse[1] < 250:
                click.play()
                Menu()
            if event.type == pygame.MOUSEBUTTONDOWN and 1900 < Mouse[0] < 1920 and 0 < Mouse[1] < 20:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        Font = pygame.font.Font("Dosis-ExtraLight.ttf", 45)
        TitleFont = pygame.font.Font("Dosis-ExtraLight.ttf", 80)
        TitleText = TitleFont.render("Instructions:", True, white)

        Background = pygame.image.load("Stars.jpg")
        Background = pygame.transform.scale(Background, size)
        Instructions.blit(Background, [0, 0])
        Instructions.blit(TitleText, [50, 30])
        pygame.draw.rect(Instructions, white, [1900, 0, 20, 20])

        if 30 < Mouse[0] < 150 and 180 < Mouse[1] < 250:
            MenuTextHover = Font.render("Menu", True, MercuryColour)
            Instructions.blit(MenuTextHover, [50, 200])
            pygame.display.update()
        else:
            MenuTextNormal = Font.render("Menu", True, white)
            Instructions.blit(MenuTextNormal, [50, 200])
            pygame.display.update()
        pygame.display.flip()


def Play():
    done = False
    SolarSystem = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    Sun = Planet("Sun", 50, SunColour, 0, 0, 0, 0, size[0] / 2, size[1] / 2)
    Mercury = Planet("Mercury", 4, MercuryColour, 0.00477, 70, 0, random.uniform(0, 6.2832), size[0] / 2, size[1] / 2)
    Venus = Planet("Sun", 5.5, VenusColour, 0.00354, 125, 0, random.uniform(0, 6.2832), size[0] / 2, size[1] / 2)
    Earth = Planet("Earth", 6, EarthColour, 0.003, 180, 0, random.uniform(0, 6.2832), size[0] / 2, size[1] / 2)
    Moon = Planet("Moon", 2, VenusColour, 0.0001029, 20, 0, random.uniform(0, 6.2832), Planet.getx(Earth), Planet.gety(Earth))
    Mars = Planet("Mars", 4, MarsColour, 0.002424, 235, 0, random.uniform(0, 6.2832), size[0] / 2, size[1] / 2)
    Jupiter = Planet("Jupiter", 17, JupiterColour, 0.001317, 290, 0, random.uniform(0, 6.2832), size[0] / 2, size[1] / 2)
    Saturn = Planet("Saturn", 12, SaturnColour, 0.000975, 345, 0, random.uniform(0, 6.2832), size[0] / 2, size[1] / 2)
    Uranus = Planet("Uranus", 10, UranusColour, 0.000684, 400, 0, random.uniform(0, 6.2832), size[0] / 2, size[1] / 2)
    Neptune = Planet("Neptune", 10, NeptuneColour, 0.000546, 455, 0, random.uniform(0, 6.2832), size[0] / 2, size[1] / 2)
    Pluto = Planet("Pluto", 4, PlutoColour, 0.000471, 510, 0, random.uniform(0, 6.2832), size[0] / 2, size[1] / 2)

    while not done:
        Background = pygame.image.load("Stars.jpg")
        Background = pygame.transform.scale(Background, size)
        SolarSystem.blit(Background, [0, 0])
        for event in pygame.event.get():
            if event.type == pygame.quit:
                done = True
            Mouse = pygame.mouse.get_pos()
            print(Mouse)
            if event.type == pygame.MOUSEBUTTONDOWN and 30 < Mouse[0] < 165 and 60 < Mouse[1] < 125:
                click.play()
                Menu()
            if event.type == pygame.MOUSEBUTTONDOWN and 30 < Mouse[0] < 195 and 155 < Mouse[1] < 220:
                click.play()
                Planet.speedUp(Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto)
            if event.type == pygame.MOUSEBUTTONDOWN and 30 < Mouse[0] < 195 and 250 < Mouse[1] < 315:
                click.play()
                Planet.slowDown(Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto)
            if event.type == pygame.MOUSEBUTTONDOWN and 30 < Mouse[0] < 150 and 345 < Mouse[1] < 410:
                click.play()
                Planet.stop(Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto)
            if event.type == pygame.MOUSEBUTTONDOWN and 30 < Mouse[0] < 150 and 440 < Mouse[1] < 505:
                click.play()
                Planet.go(Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto)
            if event.type == pygame.MOUSEBUTTONDOWN and 1900 < Mouse[0] < 1920 and 0 < Mouse[1] < 20:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        pygame.draw.rect(SolarSystem, white, [1900, 0, 20, 20])
        Font = pygame.font.Font("Dosis-ExtraLight.ttf", 45)

        Sun.render(SolarSystem)
        Mercury.render(SolarSystem)
        Venus.render(SolarSystem)
        Earth.render(SolarSystem)
        #Moon.render(SolarSystem)
        Mars.render(SolarSystem)
        Jupiter.render(SolarSystem)
        Saturn.render(SolarSystem)
        Uranus.render(SolarSystem)
        Neptune.render(SolarSystem)
        Pluto.render(SolarSystem)

        if 30 < Mouse[0] < 165 and 60 < Mouse[1] < 125:
            MenuTextHover = Font.render("Menu", True, MercuryColour)
            SpeedupNormal = Font.render("Speed +", True, white)
            SpeeddownNormal = Font.render("Speed -", True, white)
            SolarSystem.blit(MenuTextHover, [50, 65])
            SolarSystem.blit(SpeedupNormal, [50, 155])
            SolarSystem.blit(SpeeddownNormal, [50, 250])
            pygame.display.update()
        elif 30 < Mouse[0] < 195 and 155 < Mouse[1] < 220:
            MenuTextNormal = Font.render("Menu", True, white)
            SpeedupHover = Font.render("Speed +", True, MercuryColour)
            SpeeddownNormal = Font.render("Speed -", True, white)
            SolarSystem.blit(MenuTextNormal, [50, 65])
            SolarSystem.blit(SpeedupHover, [50, 155])
            SolarSystem.blit(SpeeddownNormal, [50, 250])
            pygame.display.update()
        elif 30 < Mouse[0] < 195 and 250 < Mouse[1] < 315:
            MenuTextHover = Font.render("Menu", True, white)
            SpeedupNormal = Font.render("Speed +", True, white)
            SpeeddownHover = Font.render("Speed -", True, MercuryColour)
            SolarSystem.blit(MenuTextHover, [50, 65])
            SolarSystem.blit(SpeedupNormal, [50, 155])
            SolarSystem.blit(SpeeddownHover, [50, 250])
        else:
            MenuTextNormal = Font.render("Menu", True, white)
            SpeedupNormal = Font.render("Speed +", True, white)
            SpeeddownNormal = Font.render("Speed -", True, white)
            SolarSystem.blit(MenuTextNormal, [50, 65])
            SolarSystem.blit(SpeedupNormal, [50, 155])
            SolarSystem.blit(SpeeddownNormal, [50, 250])
            pygame.display.update()

        pygame.display.flip()
        clock.tick(144)


def Menu():
    done = False
    StartMenu = pygame.display.set_mode(size)
    pygame.display.set_caption("Solar System")

    while not done:
        Background = pygame.image.load("Stars.jpg")
        Background = pygame.transform.scale(Background, size)
        StartMenu.blit(Background, [0, 0])
        for event in pygame.event.get():
            if event.type == pygame.quit:
                done = True
            Mouse = pygame.mouse.get_pos()
            print(Mouse)
            if event.type == pygame.MOUSEBUTTONDOWN and 30 < Mouse[0] < 150 and 180 < Mouse[1] < 250:
                click.play()
                Play()
            if event.type == pygame.MOUSEBUTTONDOWN and 30 < Mouse[0] < 300 and 280 < Mouse[1] < 350:
                click.play()
                Instructions()
            if event.type == pygame.MOUSEBUTTONDOWN and 30 < Mouse[0] < 300 and 380 < Mouse[1] < 450:
                click.play()
                Font = pygame.font.Font("Dosis-ExtraLight.ttf", 45)
                x = input("enter your name")
                NameInputText = Font.render(x, True, white)
                StartMenu.blit(NameInputText, [300, 380])
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN and 1900 < Mouse[0] < 1920 and 0 < Mouse[1] < 20:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        Font = pygame.font.Font("Dosis-ExtraLight.ttf", 45)
        TitleFont = pygame.font.Font("Dosis-ExtraLight.ttf", 80)

        TitleText = TitleFont.render("Welcome To The Solar System", True, white)
        StartMenu.blit(TitleText, [50, 30])
        pygame.draw.rect(StartMenu, white, [1900, 0, 20, 20])

        if 30 < Mouse[0] < 150 and 180 < Mouse[1] < 250:
            PlayTextHover = Font.render("Play!", True, MercuryColour)
            StartMenu.blit(PlayTextHover, [50, 200])
            InstructionsTextNormal = Font.render("Instructions", True, white)
            StartMenu.blit(InstructionsTextNormal, [50, 300])
            pygame.display.update()
        elif 30 < Mouse[0] < 300 and 280 < Mouse[1] < 350:
            InstructionsTextHover = Font.render("Instructions", True, MercuryColour)
            StartMenu.blit(InstructionsTextHover, [50, 300])
            PlayTextNormal = Font.render("Play!", True, white)
            StartMenu.blit(PlayTextNormal, [50, 200])
            pygame.display.update()
        else:
            PlayTextNormal = Font.render("Play!", True, white)
            StartMenu.blit(PlayTextNormal, [50, 200])
            InstructionsTextNormal = Font.render("Instructions", True, white)
            StartMenu.blit(InstructionsTextNormal, [50, 300])
            pygame.display.update()

        pygame.display.flip()


Menu()
