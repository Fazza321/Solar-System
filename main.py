import random

from PagesClass import *
from buttonClass import *
from planetClass import *

pygame.init()


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
                planetText = Font.render(Planet.getname(planet), True, white)
                SolarSystem.blit(planetText, (xa, ya))
                if ButtonDown:
                    if planet == Sun:
                        click.play()
                        SunPage()
                    if planet == Mercury:
                        click.play()
                        MercuryPage()
                    if planet == Venus:
                        click.play()
                        VenusPage()
                    if planet == Earth:
                        click.play()
                        EarthPage()
                    if planet == Moon:
                        click.play()
                        MoonPage()
                    if planet == Mars:
                        click.play()
                        MarsPage()
                    if planet == Jupiter:
                        click.play()
                        JupiterPage()
                    if planet == Saturn:
                        click.play()
                        SaturnPage()
                    if planet == Uranus:
                        click.play()
                        UranusPage()
                    if planet == Neptune:
                        click.play()
                        NeptunePage()
                    if planet == Pluto:
                        click.play()
                        PlutoPage()


        pygame.display.flip()


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


def SunPage():
    done = False
    screen = pygame.display.set_mode(size)
    TitleText = Button("Sun Info:", 50, 30, TitleFont)
    MenuText = Button("Back", 50, 200, Font)
    while not done:
        screen.blit(Background, [0, 0])
        mx, my = pygame.mouse.get_pos()
        TitleText.write(screen, white)
        MenuText.write(screen, white)
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


def MercuryPage():
    done = False
    screen = pygame.display.set_mode(size)
    TitleText = Button("Mercury Info:", 50, 30, TitleFont)
    MenuText = Button("Back", 50, 200, Font)
    while not done:
        screen.blit(Background, [0, 0])
        mx, my = pygame.mouse.get_pos()
        TitleText.write(screen, white)
        MenuText.write(screen, white)
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


def VenusPage():
    done = False
    screen = pygame.display.set_mode(size)
    TitleText = Button("Venus Info:", 50, 30, TitleFont)
    MenuText = Button("Back", 50, 200, Font)
    while not done:
        screen.blit(Background, [0, 0])
        mx, my = pygame.mouse.get_pos()
        TitleText.write(screen, white)
        MenuText.write(screen, white)
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


def EarthPage():
    done = False
    screen = pygame.display.set_mode(size)
    TitleText = Button("Earth Info:", 50, 30, TitleFont)
    MenuText = Button("Back", 50, 200, Font)
    while not done:
        screen.blit(Background, [0, 0])
        screen.blit(EarthImage, [-750, 0])
        mx, my = pygame.mouse.get_pos()
        TitleText.write(screen, white)
        MenuText.write(screen, white)
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


def MoonPage():
    done = False
    screen = pygame.display.set_mode(size)
    TitleText = Button("Moon Info:", 50, 30, TitleFont)
    MenuText = Button("Back", 50, 200, Font)
    while not done:
        screen.blit(Background, [0, 0])
        mx, my = pygame.mouse.get_pos()
        TitleText.write(screen, white)
        MenuText.write(screen, white)
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


def MarsPage():
    done = False
    screen = pygame.display.set_mode(size)
    TitleText = Button("Mars Info:", 50, 30, TitleFont)
    MenuText = Button("Back", 50, 200, Font)
    while not done:
        screen.blit(Background, [0, 0])
        mx, my = pygame.mouse.get_pos()
        TitleText.write(screen, white)
        MenuText.write(screen, white)
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


def JupiterPage():
    done = False
    screen = pygame.display.set_mode(size)
    TitleText = Button("Jupiter Info:", 50, 30, TitleFont)
    MenuText = Button("Back", 50, 200, Font)
    while not done:
        screen.blit(Background, [0, 0])
        mx, my = pygame.mouse.get_pos()
        TitleText.write(screen, white)
        MenuText.write(screen, white)
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


def SaturnPage():
    done = False
    screen = pygame.display.set_mode(size)
    TitleText = Button("Saturn Info:", 50, 30, TitleFont)
    MenuText = Button("Back", 50, 200, Font)
    while not done:
        screen.blit(Background, [0, 0])
        mx, my = pygame.mouse.get_pos()
        TitleText.write(screen, white)
        MenuText.write(screen, white)
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


def UranusPage():
    done = False
    screen = pygame.display.set_mode(size)
    TitleText = Button("Uranus Info:", 50, 30, TitleFont)
    MenuText = Button("Back", 50, 200, Font)
    while not done:
        screen.blit(Background, [0, 0])
        mx, my = pygame.mouse.get_pos()
        TitleText.write(screen, white)
        MenuText.write(screen, white)
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


def NeptunePage():
    done = False
    screen = pygame.display.set_mode(size)
    TitleText = Button("Neptune Info:", 50, 30, TitleFont)
    MenuText = Button("Back", 50, 200, Font)
    while not done:
        screen.blit(Background, [0, 0])
        mx, my = pygame.mouse.get_pos()
        TitleText.write(screen, white)
        MenuText.write(screen, white)
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


def PlutoPage():
    done = False
    screen = pygame.display.set_mode(size)
    TitleText = Button("Pluto Info:", 50, 30, TitleFont)
    MenuText = Button("Back", 50, 200, Font)
    while not done:
        screen.blit(Background, [0, 0])
        mx, my = pygame.mouse.get_pos()
        TitleText.write(screen, white)
        MenuText.write(screen, white)
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
