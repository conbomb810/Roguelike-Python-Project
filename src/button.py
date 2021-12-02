import pygame

#this doesnt work
#the button the player will use to complete certain actions
class button(pygame.sprite.Sprite):
    def __init__(self, x, y, text, size):
        super().__init__()
        pygame.font.init()
        self.font = pygame.font.SysFont(text, size)
        self.image = pygame.Surface((self.font.size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


