import pygame
import random
class monster(pygame.sprite.Sprite):
   
   def __init__(self, health, start_coordx, start_coordy):
      super().__init__()
      self.health = 200
      self.image = pygame.image.load('assets/monster.png').convert_alpha()
      self.rect = self.image.get_rect()
      self.rect.inflate_ip(25, 25)
      self.speed = 10
      self.rect.x = start_coordx
      self.rect.y = start_coordy 
      "setting parameters for starting position and also setting the health of the monster."
   def attack(self)
   "will be collision attack"   
   def move(self)
   "stationary for time being"
