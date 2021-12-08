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
      self.buttons = self.font.render(self.pretext + str(self.currentScore), False, txtColor, backColor)
      self.image = self.buttons
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y
      self.x = x
      self.y = y
      self.txtColor = txtColor
      self.backColor = backColor

   def incrementByKill(self):
      self.currentScore += 100
      self.recall()

   def incrementBonus(self, health):
      self.currentScore += (health//2)
      self.recall()

   def incrementByBoss(self):
      self.currentScore += 400
      self.recall()


   def recall(self):
      self.buttons = self.font.render(self.pretext + str(self.currentScore), False, self.txtColor, self.backColor)
      self.image = self.buttons
      self.rect = self.image.get_rect()
      self.rect.x = self.x
      self.rect.y = self.y

         
      
