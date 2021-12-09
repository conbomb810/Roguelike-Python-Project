#this tracks the score that the player acquires during the game
from src import hero
from src import monster
import pygame
#this class needs an image and rect variable, find an image to use for it, probably a font object
#this should also export the score to the highscore json file ONLY IF score > highscore
class score(pygame.sprite.Sprite):
   def __init__(self, x, y, size, txtColor, backColor):
      super().__init__()
      self.font = pygame.font.SysFont("caladea", size)
      self.pretext = "Score: "
      self.currentScore = 0
      self.scorebox = self.font.render(self.pretext + str(self.currentScore), False, txtColor, backColor)
      self.image = self.scorebox
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y
      self.x = x
      self.y = y
      self.txtColor = txtColor
      self.backColor = backColor
   """
   sets the variables for the sprite created to display the highscore on screen
   """
   def incrementByKill(self):
      self.currentScore += 100
      self.recall()
   """
   each kill increases score by 100
   """

   def incrementBonus(self, health):
      self.currentScore += (health//2)
      self.recall()
   """
   the remaining health of hero is divded by 2 then added to the score
   """

   def incrementByBoss(self):
      self.currentScore += 400
      self.recall()

   """
   when boss is killed score increase by 400
   """
   def recall(self):
      self.scorebox = self.font.render(self.pretext + str(self.currentScore), False, self.txtColor, self.backColor)
      self.image = self.scorebox
      self.rect = self.image.get_rect()
      self.rect.x = self.x
      self.rect.y = self.y
   """
   the score is updated, then rendered onto the screen
   """
         
      
