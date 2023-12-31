import pygame

#the display that shows the status of the players health.
#this works fine other than the fact that the font object doesn't change when health is updated
class healthBar(pygame.sprite.Sprite):
    def __init__(self, x, y, health, maxHealth):
        super().__init__()
        self.font = pygame.font.SysFont("caladea", 35)
        self.maxHealth = maxHealth
        self.health = health
        self.healthStr = f"{health} / {maxHealth}"
        self.bar = self.font.render(self.healthStr, False, (0,0,0), (200,0,0))
        self.image = self.bar
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
    def update(self, hp):
        """
        creates a health box using the max health of hero and the current health. The bar values are then updated after each attack.
        args: none
        return: none
        """
        self.health = hp
        if self.health >= 0:
            self.healthStr = f"{self.health} / {self.maxHealth}"
        else:
            self.healthStr = f"0 / {self.maxHealth}"
        self.bar = self.font.render(self.healthStr, False, (0,0,0), (200,0,0))
        self.image = self.bar
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        

