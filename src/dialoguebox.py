import pygame
#this where dialogue between characters or anything said to the player is displayed
#this code should be virtually the same as healthBar.py except the String should be a parameter of a method
class dialoguebox(pygame.sprite.Sprite):
	def __init__(self, x, y, text, size, textColor, backColor=None):
		super().__init__()
		self.font = pygame.font.SysFont("caladea", size)
		self.dialogue = self.font.render(text, False, textColor, backColor)
		self.image = self.dialogue
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.x = x
		self.y = y
		self.textColor = textColor
		self.backColor = backColor

	def update(self, text):
		self.dialogue = self.font.render(text, False, self.textColor, self.backColor)
		self.image = self.dialogue
		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y

