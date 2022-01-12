import random

from PagesClass import *
from buttonClass import *
from planetClass import *

pygame.init()


def Menu():
    done = False
    StartMenu = pygame.display.set_mode(size)

    TitleText = Button("Welcome To The Solar System", 50, 30, TitleFont)
    PlayText = Button("Play!", 50, 200, Font)
    InstructionsText = Button("Instructions", 50, 300, Font)

    while not done:
        StartMenu.blit(Background, [0, 0])
        mx, my = pygame.mouse.get_pos()
        ButtonDown = False
        PlayText.write(StartMenu, white)
        InstructionsText.write(StartMenu, white)
        TitleText.write(StartMenu, white)

        for event in pygame.event.get():
            if event.type == pygame.quit:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                ButtonDown = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        PlayButton = pygame.Rect(30, 180, 120, 70)
        if PlayButton.collidepoint((mx, my)):
            PlayText.write(StartMenu, MercuryColour)
            if ButtonDown:
                click.play()
                Play()
        InstructionsButton = pygame.Rect(30, 280, 270, 70)
        if InstructionsButton.collidepoint((mx, my)):
            InstructionsText.write(StartMenu, MercuryColour)
            if ButtonDown:
                click.play()
                Instructions()
        ExitButton = pygame.draw.rect(StartMenu, white, [1900, 0, 20, 20])
        if ExitButton.collidepoint((mx, my)):
            pygame.draw.rect(StartMenu, MercuryColour, [1900, 0, 20, 20])
            if ButtonDown:
                click.play()
                pygame.time.wait(150)
                pygame.quit()

        pygame.display.flip()


def Instructions():
    done = False
    Instructions = pygame.display.set_mode(size)
    TitleText = Button("Instructions:", 50, 30, TitleFont)
    MenuText = Button("Menu", 50, 200, Font)
    while not done:
        Instructions.blit(Background, [0, 0])
        mx, my = pygame.mouse.get_pos()
        TitleText.write(Instructions, white)
        MenuText.write(Instructions, white)
        ButtonDown = False

        for event in pygame.event.get():
            if event.type == pygame.quit:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                ButtonDown = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        ExitButton = pygame.draw.rect(Instructions, white, [1900, 0, 20, 20])
        if ExitButton.collidepoint(mx, my):
            pygame.draw.rect(Instructions, MercuryColour, [1900, 0, 20, 20])
            if ButtonDown:
                click.play()
                pygame.time.wait(160)
                pygame.quit()
        MenuButton = pygame.Rect(30, 180, 120, 70)
        if MenuButton.collidepoint((mx, my)):
            MenuText.write(Instructions, MercuryColour)
            if ButtonDown:
                click.play()
                Menu()

        pygame.display.flip()


def Play():
    done = False
    SolarSystem = pygame.display.set_mode(size)

    Sun = Planet("Sun", 50, SunColour, 0, 0, 0, 0, None, (size[0] / 2, size[1] / 2))
    Mercury = Planet(
        "Mercury",
        4,
        MercuryColour,
        0.00477,
        70,
        0,
        random.uniform(0, 6.2832),
        Sun,
        (size[0] / 2, size[1] / 2),
    )
    Venus = Planet(
        "Venus",
        5.5,
        VenusColour,
        0.00354,
        125,
        0,
        random.uniform(0, 6.2832),
        Sun,
        (size[0] / 2, size[1] / 2),
    )
    Earth = Planet(
        "Earth",
        6,
        EarthColour,
        0.003,
        180,
        0,
        random.uniform(0, 6.2832),
        Sun,
        (size[0] / 2, size[1] / 2),
    )
    Moon = Planet(
        "Moon",
        2,
        VenusColour,
        0.015,
        20,
        0,
        random.uniform(0, 6.2832),
        Earth,
        (size[0] / 2, size[1] / 2),
    )
    Mars = Planet(
        "Mars",
        4,
        MarsColour,
        0.002424,
        235,
        0,
        random.uniform(0, 6.2832),
        Sun,
        (size[0] / 2, size[1] / 2),
    )
    Jupiter = Planet(
        "Jupiter",
        17,
        JupiterColour,
        0.001317,
        290,
        0,
        random.uniform(0, 6.2832),
        Sun,
        (size[0] / 2, size[1] / 2),
    )
    Saturn = Planet(
        "Saturn",
        12,
        SaturnColour,
        0.000975,
        345,
        0,
        random.uniform(0, 6.2832),
        Sun,
        (size[0] / 2, size[1] / 2),
    )
    Uranus = Planet(
        "Uranus",
        10,
        UranusColour,
        0.000684,
        400,
        0,
        random.uniform(0, 6.2832),
        Sun,
        (size[0] / 2, size[1] / 2),
    )
    Neptune = Planet(
        "Neptune",
        10,
        NeptuneColour,
        0.000546,
        455,
        0,
        random.uniform(0, 6.2832),
        Sun,
        (size[0] / 2, size[1] / 2),
    )
    Pluto = Planet(
        "Pluto",
        4,
        PlutoColour,
        0.000471,
        510,
        0,
        random.uniform(0, 6.2832),
        Sun,
        (size[0] / 2, size[1] / 2),
    )
    Planets = [
        Sun,
        Mercury,
        Venus,
        Earth,
        Mars,
        Jupiter,
        Saturn,
        Uranus,
        Neptune,
        Pluto,
        Moon,
    ]

    SolarSystemText = Button("The Solar System", 50, 30, TitleFont)
    MenuText = Button("Menu", 50, 200, Font)
    SpeedUpText = Button("Speed +", 50, 300, Font)
    SpeedDownText = Button("Speed -", 50, 400, Font)
    StopText = Button("Stop", 50, 500, Font)

    while not done:
        SolarSystem.blit(Background, [0, 0])
        mx, my = pygame.mouse.get_pos()
        ButtonDown = False
        SolarSystemText.write(SolarSystem, white)
        SpeedUpText.write(SolarSystem, white)
        SpeedDownText.write(SolarSystem, white)
        MenuText.write(SolarSystem, white)
        StopText.write(SolarSystem, white)

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
                click.play()
                pygame.time.wait(150)
                pygame.quit()

        for planet in Planets:
            xa = Planet.centre_xa(planet)
            ya = Planet.centre_ya(planet)
            if xa - 60 < mx < xa + 60 and ya - 60 < my < ya + 60:
                planetText = Font.render(planet.getattr("name"), True, white)
                SolarSystem.blit(planetText, (xa, ya))
                if ButtonDown:
                    if planet == Sun:
                        click.play()
                        FactsPage("Mass: 1.989 × 10^30 kg", "Surface Area: ", "Radius: 696,340 km", "Age: ", "Gravitational Pull: ", "Velocity: 200 km/s", "Sun Info: ", SunImage, -750, -200)
                    if planet == Mercury:
                        click.play()
                        FactsPage("Mass: 3.285 × 10^23 kg", "Surface Area: ", "Radius: 2,439.7 km", "Age: ", "Gravitational Pull: ", "Velocity: ", "Mercury Info: ", MercuryImage, -750, -100)
                    if planet == Venus:
                        click.play()
                        FactsPage("Mass: 4.867 × 10^24 kg", "Surface Area: ", "Radius: 6,051.8 km", "Age: ", "Gravitational Pull: ", "Velocity: ", "Venus Info: ", VenusImage, -750, -150)
                    if planet == Earth:
                        click.play()
                        FactsPage("Mass: 5.9722 × 10^24 kg", "Surface Area: ", "Radius: 6,371 km", "Age: ", "Gravitational Pull: ", "Velocity: ", "Earth Info: ", EarthImage, -750, -150)
                    if planet == Moon:
                        click.play()
                        FactsPage("Mass: 7.3477 × 10^22 kg", "Surface Area: ", "Radius: 1,737.4 km", "Age: ", "Gravitational Pull: ", "Velocity: 1.023 km/s", "Moon Info: ", MoonImage, -750, -100)
                    if planet == Mars:
                        click.play()
                        FactsPage("Mass: 6.39 × 10^23 kg", "Surface Area: ", "Radius: 3,389.5 km", "Age: ", "Gravitational Pull: ", "Velocity: ", "Mars Info: ", MarsImage, -750, -100)
                    if planet == Jupiter:
                        click.play()
                        FactsPage("Mass: 1.898 × 10^27 kg", "Surface Area: ", "Radius: 69,911 km", "Age: ", "Gravitational Pull: ", "Velocity: ", "Jupiter Info: ", JupiterImage, -750, -100)
                    if planet == Saturn:
                        click.play()
                        FactsPage("Mass: 5.683 × 10^26 kg", "Surface Area: ", "Radius: 58,232 km", "Age: ", "Gravitational Pull: ", "Velocity: ", "Saturn Info: ", SaturnImage, -1350, -200)
                    if planet == Uranus:
                        click.play()
                        FactsPage("Mass: 8.681 × 10^25 kg", "Surface Area: ", "Radius: 25,362 km", "Age: ", "Gravitational Pull: ", "Velocity: ", "Uranus Info: ", UranusImage, -750, -100)
                    if planet == Neptune:
                        click.play()
                        FactsPage("Mass: 1.024 × 10^26 kg", "Surface Area: ", "Radius: 24,622 km", "Age: ", "Gravitational Pull: ", "Velocity: ", "Neptune Info: ", NeptuneImage, -750, -100)
                    if planet == Pluto:
                        click.play()
                        FactsPage("Mass: 1.30900 × 1022 kg", "Surface Area: ", "Radius: 1,188.3 km", "Age: ", "Gravitational Pull: ", "Velocity: ", "Pluto Info: ", PlutoImage, -750, -150)


        pygame.display.flip()


def FactsPage(Text1, Text2, Text3, Text4, Text5, Text6, TitleText, planetImage, x, y):
    done = False
    screen = pygame.display.set_mode(size)
    TitleText = Button(TitleText, 50, 30, TitleFont)
    MenuText = Button("Back", 50, 200, Font)
    Info1 = Button(Text1, 500, 30, Font)
    Info2 = Button(Text2, 500, 180, Font)
    Info3 = Button(Text3, 500, 330, Font)
    Info4 = Button(Text4, 500, 480, Font)
    Info5 = Button(Text5, 500, 630, Font)
    Info6 = Button(Text6, 500, 780, Font)
    while not done:
        screen.blit(Background, [0, 0])
        screen.blit(planetImage, [x, y])
        mx, my = pygame.mouse.get_pos()
        TitleText.write(screen, white)
        MenuText.write(screen, white)
        Info1.write(screen, white)
        Info2.write(screen, white)
        Info3.write(screen, white)
        Info4.write(screen, white)
        Info5.write(screen, white)
        Info6.write(screen, white)
        ButtonDown = False

        for event in pygame.event.get():
            if event.type == pygame.quit:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                ButtonDown = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        ExitButton = pygame.draw.rect(screen, white, [1900, 0, 20, 20])
        if ExitButton.collidepoint(mx, my):
            pygame.draw.rect(screen, MercuryColour, [1900, 0, 20, 20])
            if ButtonDown:
                click.play()
                pygame.time.wait(160)
                pygame.quit()
        MenuButton = pygame.Rect(30, 180, 120, 70)
        if MenuButton.collidepoint((mx, my)):
            MenuText.write(screen, MercuryColour)
            if ButtonDown:
                click.play()
                Play()

        pygame.display.flip()


Menu()
