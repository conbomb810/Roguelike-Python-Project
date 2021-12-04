import pygame
import random
class monster(pygame.sprite.Sprite):
   
   def __init__(self, health, x, y):
#need to import hero class data from text file
      super().__init__()
      self.image = pygame.image.load('assets/monsterSmall.jpg').convert_alpha()
      self.rect = self.image.get_rect()
      self.rect.inflate_ip(25, 25)
      self.alive = True
      self.rect.x = x
      self.rect.y = y 
      self.health = health
      self.max_health = self.health
      self.bar_len = 400
      #self.health.ratio = self.max_health/self.bar_len
      """setting parameters for starting position and also setting the health of the monster."""
   
   def draw(self):
      self.blit(self.image, (self.rect.x, self.rect.y))

   def attack(self, hero): #damage
      if hero.defend == False:
         damage = random.randint(0, 50)
         hero.health -= damage
         if hero.health < 1:
            hero.health = 0
            hero.alive = False
      else:
         hero.health = hero.health
         hero.defend = False

      print("damage to hero:" + str(damage))
   """
   calculates damage and adds randomized amount to it, then substracts that from health of hero
   """
   def update(self, hero):
         self.attack(hero)

   def deathCheck(self):
      if self.health == 0:
         self.image = pygame.image.load('assets/monsterDead.jpg').convert_alpha()
      

   def get_damage(self, amount):
      if self.health > 0:
         self.current_health -+ amount
      if self.health <= 0:
         self.health = 0
         self.alive = False

   """sets damage"""
   def get_health(self, amount):
      if self.health < self.max_health:
         self.health += amount
      if self.health >= self.max_health:
         self.health = self.max_health
#for getdamage and get healthfunc, must be added to event loop. when monster attacks hero health bar must go down
   """keeps health inside bar"""
   #def hero_health(self):
      #pygmae.draw.rect(screen, (250, 0, 0), (10, 10, self.health/self.health_ratio, 25)
      #pygame.draw.rect(screen, (250, 250, 250), (10, 10, self.bar_len, 25), 4)
      #values must be edited for size of window   
 

