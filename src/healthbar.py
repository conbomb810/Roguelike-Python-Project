#The health bar for the hero, goes down as health is lost.
class healthbar:
	def __init__(self, x, y):
		self.rect.x = x
		self.rect.y = y
		self.rect.fill = 'red'
	
	def losthealth(self):
	
	
