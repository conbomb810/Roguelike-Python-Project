import pygame

#the display that shows the status of the players health.
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

    def update(self, hp):
        #current = self.health - hp
        self.health = hp
        #print(self.health)
        if self.health >= 0:
            self.healthStr = f"{self.health} / {self.maxHealth}"
        else:
            self.healthStr = f"0 / {self.maxHealth}"

        self.bar = self.font.render(self.healthStr, False, (0,0,0), (200,0,0))
