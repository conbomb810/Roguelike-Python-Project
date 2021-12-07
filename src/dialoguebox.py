import pygame
#this where dialogue between characters or anything said to the player is displayed
#this code should be virtually the same as healthBar.py except the String should be a parameter of a method
class dialoguebox:
	def __init__(self, x, y, text, size, textColor, backColor):
		super().__init__()
		self.text = pygame.font.SysFont("caladea", size)
		self.dialogue = self.text.render(text, False, textColor, backColor)
		self.image = self.dialogue
        	self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.x = x
		self.y = y

	def update(self, text):
		self.bar = self.font.render(text, False, (0,0,0), (200,0,0))
        	self.image = self.dialouge
        	self.rect = self.image.get_rect()
        	self.rect.x = self.x
        	self.rect.y = self.y

