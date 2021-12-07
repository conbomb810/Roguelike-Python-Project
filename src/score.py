#this tracks the score that the player acquires during the game
from src import hero
from src import monster
import pygame
#this class needs an image and rect variable, find an image to use for it, probably a font object
#this should also export the score to the highscore json file ONLY IF score > highscore
class score(pygame.sprite.Sprite):
   def __init__(self, x, y, text, size, txtColor, backColor):
      super().__init__()
      self.font = pygame.font.SysFont("caladea", size)
      self.buttons = self.font.render(text, False, txtColor, backColor)
      self.image = self.buttons
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y
      self.score = 0
      

   def incrementByKill(self):
      self.score += 100

   def incrementBonus(self, health):
      self.score += health//2

   def incrementBossKill(self):
      self.score+= 400

         
      
