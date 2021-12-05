import pygame
#this where dialogue between characters or anything said to the player is displayed
#this code should be virtually the same as healthBar.py except the String should be a parameter of a method
class dialoguebox:
	def __init__(self, x, y, text, size, textColor, backColor):
		super().__init__()
		self.text = pygame.font.SysFont("caladea", size)
		self.dialogue = self.text.render(text, False, textColor, backColor)
		self.rect.x = x
		self.rect.y = y
	
	def __str__(self):
		
