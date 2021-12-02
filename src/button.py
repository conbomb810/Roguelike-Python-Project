import pygame

#the button the player will use to complete certain actions
class button(pygame.sprite.Sprite):
    def __init__(self, x, y, text, size, txtColor, backColor):
        super().__init__()
        self.font = pygame.font.SysFont("caladea", size)
        self.buttons = self.font.render(text, False, txtColor, backColor)
        self.image = self.buttons
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


