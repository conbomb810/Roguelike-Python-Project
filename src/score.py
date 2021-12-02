#this tracks the score that the player acquires during the game
from src import hero.py
from src import monster.py
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
         
      
