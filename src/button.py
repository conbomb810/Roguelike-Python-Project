import pygame

#the button the player will use to complete certain actions
class button(pygame.sprite.Sprite):
	def __init__(self, x, y, filePath):
		super().__init__()
		self.image = pygame.image.load(filePath)
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
                
		
	def onButtonPress(self):
