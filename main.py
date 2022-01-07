import random
import os

from pygame import mixer

from planetClass import *

from buttonClass import *

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
size = (1920, 1080)
click = mixer.Sound(os.path.join("static", "buttonclick.wav"))
Font = pygame.font.Font(os.path.join("static", "Dosis-ExtraLight.ttf"), 45)
TitleFont = pygame.font.Font(os.path.join("static", "Dosis-ExtraLight.ttf"), 80)
Background = pygame.image.load(os.path.join("static", "Stars.jpg"))
Background = pygame.transform.scale(Background, size)


def Instructions():
    done = False
    ButtonDown = False
    Instructions = pygame.display.set_mode(size)
    TitleText = Button("Instructions:", 50, 30, TitleFont)
    MenuText = Button("Menu", 50, 200, Font)
    while not done:
        Instructions.blit(Background, [0, 0])
        mx, my = pygame.mouse.get_pos()
        TitleText.write(Instructions, white)
        MenuText.write(Instructions, white)

        ExitButton = pygame.draw.rect(Instructions, white, [1900, 0, 20, 20])
        if ExitButton.collidepoint(mx, my) and ButtonDown:
            pygame.quit()
        MenuButton = pygame.Rect(30, 180, 120, 70)
        if MenuButton.collidepoint((mx, my)):
            MenuText.write(Instructions, MercuryColour)
            if ButtonDown:
                click.play()
                Menu()

        for event in pygame.event.get():
            if event.type == pygame.quit:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                ButtonDown = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        pygame.display.flip()


def Play():
    done = False
    ButtonDown = False
    SolarSystem = pygame.display.set_mode(size)

    Sun = Planet("Sun", 50, SunColour, 0, 0, 0, 0, None, (size[0] / 2, size[1] / 2))
    Mercury = Planet("Mercury", 4, MercuryColour, 0.00477, 70, 0, random.uniform(0, 6.2832), Sun, (size[0] / 2, size[1] / 2))
    Venus = Planet("Sun", 5.5, VenusColour, 0.00354, 125, 0, random.uniform(0, 6.2832), Sun, (size[0] / 2, size[1] / 2))
    Earth = Planet("Earth", 6, EarthColour, 0.003, 180, 0, random.uniform(0, 6.2832), Sun, (size[0] / 2, size[1] / 2))
    Moon = Planet("Moon", 2, VenusColour, 0.015, 20, 0, random.uniform(0, 6.2832), Earth, (size[0] / 2, size[1] / 2))
    Mars = Planet("Mars", 4, MarsColour, 0.002424, 235, 0, random.uniform(0, 6.2832), Sun, (size[0] / 2, size[1] / 2))
    Jupiter = Planet("Jupiter", 17, JupiterColour, 0.001317, 290, 0, random.uniform(0, 6.2832), Sun, (size[0] / 2, size[1] / 2))
    Saturn = Planet("Saturn", 12, SaturnColour, 0.000975, 345, 0, random.uniform(0, 6.2832), Sun, (size[0] / 2, size[1] / 2))
    Uranus = Planet("Uranus", 10, UranusColour, 0.000684, 400, 0, random.uniform(0, 6.2832), Sun, (size[0] / 2, size[1] / 2))
    Neptune = Planet("Neptune", 10, NeptuneColour, 0.000546, 455, 0, random.uniform(0, 6.2832), Sun, (size[0] / 2, size[1] / 2))
    Pluto = Planet("Pluto", 4, PlutoColour, 0.000471, 510, 0, random.uniform(0, 6.2832), Sun, (size[0] / 2, size[1] / 2))
    Planets = [Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Moon]

    SolarSystemText = Button("The Solar System", 50, 30, TitleFont)
    MenuText = Button("Menu", 50, 200, Font)
    SpeedUpText = Button("Speed +", 50, 300, Font)
    SpeedDownText = Button("Speed -", 50, 400, Font)
    StopText = Button("Stop", 50, 500, Font)

    while not done:
        SolarSystem.blit(Background, [0, 0])
        mx, my = pygame.mouse.get_pos()
        SolarSystemText.write(SolarSystem, white)
        SpeedUpText.write(SolarSystem, white)
        SpeedDownText.write(SolarSystem, white)
        MenuText.write(SolarSystem, white)
        StopText.write(SolarSystem, white)

        for event in pygame.event.get():
            if event.type == pygame.quit:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                ButtonDown = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        MenuButton = pygame.Rect(30, 200, 135, 50)
        if MenuButton.collidepoint((mx, my)):
            MenuText.write(SolarSystem, MercuryColour)
            if ButtonDown:
                click.play()
                Menu()
        SpeedUpButton = pygame.Rect(30, 300, 165, 50)
        if SpeedUpButton.collidepoint((mx, my)):
            SpeedUpText.write(SolarSystem, MercuryColour)
            if ButtonDown:
                click.play()
                Planet.speedUp(Planets)
        SpeedDownButton = pygame.Rect(30, 400, 165, 50)
        if SpeedDownButton.collidepoint((mx, my)):
            SpeedDownText.write(SolarSystem, MercuryColour)
            if ButtonDown:
                click.play()
                Planet.slowDown(Planets)
        StopButton = pygame.Rect(30, 500, 110, 50)
        if StopButton.collidepoint((mx, my)):
            StopText.write(SolarSystem, MercuryColour)
            if ButtonDown:
                click.play()
                Planet.stop(Planets)
        ExitButton = pygame.draw.rect(SolarSystem, white, [1900, 0, 20, 20])
        if ExitButton.collidepoint((mx, my)):
            pygame.draw.rect(SolarSystem, MercuryColour, [1900, 0, 20, 20])
            if ButtonDown:
                pygame.quit()

        Sun.render(SolarSystem)
        Mercury.render(SolarSystem)
        Venus.render(SolarSystem)
        Earth.render(SolarSystem)
        Moon.render(SolarSystem)
        Mars.render(SolarSystem)
        Jupiter.render(SolarSystem)
        Saturn.render(SolarSystem)
        Uranus.render(SolarSystem)
        Neptune.render(SolarSystem)
        Pluto.render(SolarSystem)

        pygame.display.flip()


def Menu():
    done = False
    StartMenu = pygame.display.set_mode(size)

    TitleText = Button("Welcome To The Solar System", 50, 30, TitleFont)
    PlayText = Button("Play!", 50, 200, Font)
    InstructionsText = Button("Instructions", 50, 300, Font)

    while not done:
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
                x = input("enter your name")
                NameInputText = Font.render(x, True, white)
                StartMenu.blit(NameInputText, [300, 380])
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN and 1900 < Mouse[0] < 1920 and 0 < Mouse[1] < 20:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        pygame.draw.rect(StartMenu, white, [1900, 0, 20, 20])

        PlayText.write(StartMenu, white)
        InstructionsText.write(StartMenu, white)
        TitleText.write(StartMenu, white)

        if 30 < Mouse[0] < 150 and 180 < Mouse[1] < 250:
            PlayText.write(StartMenu, MercuryColour)
        elif 30 < Mouse[0] < 300 and 280 < Mouse[1] < 350:
            InstructionsText.write(StartMenu, MercuryColour)
        pygame.display.flip()


Menu()

