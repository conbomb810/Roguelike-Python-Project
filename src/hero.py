import pygame
import random


class Hero(pygame.sprite.Sprite):
   def __init__(self, name, health, mana, potion, strength, magic, x, y, image):
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
      self.mana = mana
      self.maxMana = mana
      self.health = health
      self.max_health = self.health
      self.bar_len = 400
      #self.health.ratio = self.max_health/self.bar_len
   #all stats can change based on what class is chosen, this is for testing. 
   
   def draw(self):
      self.blit(self.image, (self.rect.x, self.rect.y))

   
   def update(self):
      if self.health <= 0:
         self.alive = False

   def attack(self, monster, dialogue): #damage to monster
      rand = random.randint(0, 50)
      damage = self.strength + rand
      monster.health -= damage
      if monster.health < 1:
         monster.health = 0
         monster.alive = False
      dialogue.update("monster health remaining:" + str(monster.health))
      dialogue.update("damage to monster:" + str(damage))
      """
      calculates damage based off of strength and randomizer, that amount is then taken off of the enemies health
      args: none
      return: none
      """
   
   def useMagic(self, monster, dialogue):
      if self.mana - 10 >= 0:
         rand = random.randint(0, 20)
         damage = self.magic + rand
         monster.health -= damage
         if monster.health < 1:
            monster.health = 0
            monster.alive = False
         self.mana -= 10
         dialogue.update("monster health remaining: " + str(monster.health))
         dialogue.update("damage to monster: " + str(damage))
         return True
      else:
         dialogue.update("Not enough mana, select another action")
         return False
      """
      additional move for hero to attack monsters that uses mana bar model
      args: none
      return: True, False
      """

   def useItem(self, dialogue, dialogue2):
      if self.item_use > 0:
         heal = self.health + self.item
         if (heal) <= self.max_health:
            self.health = heal
            dialogue.update("Health restored: " + str(self.item))
         else:
            self.health = self.max_health
            dialogue.update("Health completely restored")
         self.item_use -= 1
         dialogue2.update("items remaining: " + str(self.item_use))
         return True
      else:
         return False
      """
      gives hero the function to use items such as potions to increase health up to 3 times
      args: none
      return: none
      """
      
   def defending(self):
      self.defend = True

   def get_damage(self, amount):
      if self.health > 0:
         self.health =  self.health - amount
      else:
         self.health = 0
   """
   sets damage applied to hero
   args: none
   return: none
   """

   def get_health(self, amount):
      if self.health < self.max_health:
         self.health += amount
      if self.health >= self.max_health:
         self.health = self.max_health
#for getdamage and get healthfunc, must be added to event loop. when monster attacks hero health bar must go down
   """
   gets the health of the hero
   args: none
   return: none
   """

   def hero_health(self):
      #just makeit pass back a number for now
      #pygmae.draw.rect(screen, (250, 0, 0), (10, 10, self.health/self.health_ratio, 25)
      #pygame.draw.rect(screen, (250, 250, 250), (10, 10, self.bar_len, 25), 4)
      #values must be edited for size of window
      pass
