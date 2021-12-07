#this tracks the score that the player acquires during the game
from src import hero
from src import monster

#this class needs an image and rect variable, find an image to use for it, probably a font object
#this should also export the score to the highscore json file ONLY IF score > highscore
class score:
	def __init__(self):
		self.start_score = 0
		self.increment = 100
		self.bonus = hero.health // 2
	
	def update(self):
		if monster.health < 1:
			self.score += self.increment
			self.score += self.bonus
		return self.score
         
      
