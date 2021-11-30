import pygame
import random

class Hero(pygame.sprite.Sprites):
   def __init__(self):
      super().__init__()
      self.direction = 'R'
      self.image = pygame.image.load('assets/samarai.png').convert_alpha()
      self.rect = self.image.get_rect()
      self.rect.inflate_ip(-25, 25)
      self.speed = 15
      self.rect.x = 10
      self.rect.y = 10
      self.hitbox = (40, 20, 20, 50) 
      self.health = 200
      self.max_health
      self.bar_len = 400
      self.health.ratio = self.max_health/self.bar_len
   """sets image for characted adjust size, also sets size of hitbox for collision attacks"""
   
   def move(self.direction)
      if direction == "U":
         self.rect.y -= self.speed
      elif direction == "D":
         self.rect.y += self.speed
      elif direction == "L":
         self.rect.x += self.speed
      elif+direction == "R":
         self.rect x -= self.speed
   """the vertical and horizontal movement for character"""
  
   def getDamage(self, amount):
      if self.health > 0:
         self.current_health -+ amount
      if self.health =< 0:
         self.health = 0

"""sets damage"""
   def getHealth(self, amount)
      if self.health < self.max_health:
         self.health += amount
      if self.health >= self.max_health:
         self.health = self.max_health
#for getdamage and get healthfunc, must be added to event loop. when monster attacks hero health bar must go down
"""keeps health inside bar"""
   def heroHealth(self)
      pygmae.draw.rect(screen, (250, 0, 0), (10, 10, self.health/self.health_ratio, 25)
      pygame.draw.rect(screen, (250, 250, 250), (10, 10, self.bar_len, 25), 4)
         
   def healthBar(self)
   def attack(self)
      
   def defend(self)
   
   
