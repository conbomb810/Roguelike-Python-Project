import pygame
import random

#need to import monster datat from text file
#Shrink the size of the image to a manageable level
#Allow controller to send arguments for the position of the Hero's image on screen (rect.x and rect.y i believe)
#Make a list of moves the Hero can choose from

class Hero(pygame.sprite.Sprite):
   def __init__(self, name, health, potion, strength, magic, x, y, image):
      super().__init__()
      self.image = pygame.image.load(image).convert_alpha()
      self.rect = self.image.get_rect()
      self.rect.inflate_ip(-25, 25)
      self.rect.x = x
      self.rect.y = y
      self.alive = True
      self.defend = False
      self.name = name
      self.item = potion
      self.item_use = 3
      self.strength = strength
      self.magic = magic
      self.health = health
      self.max_health = self.health
      self.bar_len = 400
      #self.health.ratio = self.max_health/self.bar_len
   #all stats can change based on what class is chosen, this is for testing. 
   """sets image for characted adjust size, also sets size of hitbox for collision attacks"""
   
   def draw(self):
      self.blit(self.image, (self.rect.x, self.rect.y))

   
   def update(self):
      if self.health <= 0:
         self.alive = False

   def attack(self, monster): #damage to monster
      """
      calculates damage based off of strength and randomizer, that amount is then taken off of the enemies health
      """
      rand = random.randint(0, 50)
      damage = self.strength + rand
      monster.health -= damage
      if monster.health < 1:
         monster.health = 0
         monster.alive = False
      print("monster health remaining:" + str(monster.health))
      print("damage to monster:" + str(damage))
   
   def useMagic(self, monster, dialogue):
      rand = random.randint(0, 20)
      damage = self.magic + rand
      monster.health -= damage
      if monster.health < 1:
         monster.health = 0
         monster.alive = False
      dialogue.update("monster health remaining:" + str(monster.health))
      dialogue.update("damage to monster:" + str(damage))

   def useItem(self):
      if self.item_use > 0:
         if (self.health + self.item) <= self.max_health:
            self.health = self.health + self.item
         else:
            self.health = self.max_health
         self.item_use -= 1
         print ("items remaining" + str(self.item_use))
         return True
      else:
         return False
      
   def defending(self):
      self.defend = True

   def get_damage(self, amount):
      if self.health > 0:
         self.health =  self.health - amount
      else:
         self.health = 0
   """
   sets damage
   """

   def get_health(self, amount):
      if self.health < self.max_health:
         self.health += amount
      if self.health >= self.max_health:
         self.health = self.max_health
#for getdamage and get healthfunc, must be added to event loop. when monster attacks hero health bar must go down


   def hero_health(self):
      """keeps health inside bar"""
      #just makeit pass back a number for now
      #pygmae.draw.rect(screen, (250, 0, 0), (10, 10, self.health/self.health_ratio, 25)
      #pygame.draw.rect(screen, (250, 250, 250), (10, 10, self.bar_len, 25), 4)
      #values must be edited for size of window
      pass
