class Button:
    def __init__(self, name, x, y, font):
        self.name = name
        self.x = x
        self.y = y
        self.font = font

    def write(self, screenType, col):
        text = self.font.render(self.name, True, col)
        screenType.blit(text, (self.x, self.y))
