import pygame
#this code should be the literal same thing as healthBar.py but with mana instead of health
#using magic will decrease the overall "hp" of the class
class manaBar(pygame.sprite.Sprite):
	def __init__(self, x, y, mana, maxMana):
		super().__init__()
		self.font = pygame.font.SysFont("caladea", 35)
		self.mana = mana
		self.maxMana = maxMana
		self.manaStr = f"{mana} / {maxMana}"
		self.bar = self.font.render(self.manaStr, False, (0,0,0), (0,0,200))
		self.image = self.bar
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.x = x
		self.y = y
        
	def update(self, mana):
		self.mana = mana
		if self.mana >= 0:
			self.manaStr = f"{self.mana} / {self.maxMana}"
		else:
			self.manaStr = f"0 / {self.maxMana}"
		self.bar = self.font.render(self.manaStr, False, (0,0,0), (0,0,200))
		self.image = self.bar
		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y

	
