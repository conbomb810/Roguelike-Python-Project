import pygame
import json
import random
#from src import highscore
from src import hero
from src import button
from src import monster
from src import healthBar
from src import score
from src import dialoguebox

#LIST OF THINGS I CAN'T DO BECAUSE I DON'T HAVE THEIR MODELS/THEY ARENT WORKING:
#put docstrings into models
#dialoguebox
#highscore
#score
#mana
#healthBar
#make hero.py get x and y values as parameters [[[DONE]]]
#hero.item: add limited usage and health limit
#hero.magic [[[DONE]]]
#implement mana system into hero.magic
#hero.defend [[[DONE]]]

#LIST OF THINGS I NEED TO WORK:
#monster removing it's own attack capabilities when alive = False [[[DONE]]]

#LIST OF THINGS TO IMPLEMENT (not including the above):
#multiple enemies [[[DONE]]]
#multiple fights [[[DONE]]]
#animations?
#music
#JSON compatability [[[DONE]]]

class controller:
    def __init__(self):
        """
        This is to instantiate the controller class and set everything up for other methods
        Args: None
        Return: None
        """
        self.screenWidth = 1280
        self.screenHeight = 720
        

        pygame.init()
        pygame.mixer.init()
        self.state = "startMenu"
        

        #font stuff
        pygame.font.init()

        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.background1 = pygame.image.load("assets/mountainTestBackground.jpg").convert_alpha()
        self.background2 = pygame.Surface((self.screenWidth, self.screenHeight))
        self.background2.fill((170, 170, 170))
        self.deathBackground = pygame.Surface((self.screenWidth, self.screenHeight))
        self.deathBackground.fill((255, 0, 0))
        self.winBackground = pygame.Surface((self.screenWidth, self.screenHeight))
        self.winBackground.fill((0, 200, 0))
        self.battleBackground = pygame.image.load("assets/battleBackground.jpg").convert_alpha()
        self.moveBox = pygame.image.load("assets/moveBox.png").convert_alpha()
        self.dialogueBox = pygame.image.load("assets/dialogueBoxNew.png").convert_alpha()
        self.dialogue = dialoguebox.dialoguebox(30, 600, "Battle 1/3", 48, (255,255,255))

        #self.score = score.score(x, y)
        #self.highScore = highscore.highscore(x, y) #read from json file

        self.startButton = button.button(self.screenWidth/2, self.screenHeight/2, "Start", 48, (0,0,0), (255,255,255))
        self.quitButton = button.button(self.screenWidth/2, self.screenHeight*3/4, "Quit", 48, (0,0,0), (255,0,0))
        self.attackButton = button.button(1090, 70, "Attack", 35, (255,255,255), None)
        self.magicButton = button.button(1090, 110, "Magic", 35, (255,255,255), None)
        self.itemButton = button.button(1090, 150, "Item", 35, (255,255,255), None)
        self.defendButton = button.button(1090, 190, "Defend", 35, (255,255,255), None)
        self.youSuck = button.button(self.screenWidth/3, 100, "GAME OVER, YOU SUCK", 35, (0,0,0), None)
        self.victory = button.button(self.screenWidth/2, 100, "VICTORY!", 35, (0,0,0), None)

        self.target = None

        self.hero = None
        self.heroHealthBar = None
        #self.highscore = highscore.highscore(500, 200)


        #read in JSON file with all of the maps in the game and randomly pick one to use
        fptr = open("src/info.json", 'r')
        maps = json.load(fptr)
        self.map = maps.get(random.choice(list(maps)))
        fptr.close()

        #the following sets up the battles using the chosen map
        self.monsters1 = pygame.sprite.Group()
        self.monsters2 = pygame.sprite.Group()
        self.monsters3 = pygame.sprite.Group()
        self.battles = [self.monsters1, self.monsters2, self.monsters3]

        self.monstersAlive1 = 1
        self.monstersAlive2 = 1
        self.monstersAlive3 = 1
        self.enemyCount = [self.monstersAlive1, self.monstersAlive2, self.monstersAlive3]
        
        boss = False
        count = 0
        i = 0
        for battle in self.map:
            for monst in battle:
                if monst.get("type") == "boss":
                    boss = True
                else:
                    boss = False
                self.battles[i].add(monster.monster(monst.get("hp"), monst.get("x"), monst.get("y"), monst.get("type"), monst.get("strength"), boss))
                count += 1
            self.enemyCount[i] = count
            count = 0
            i += 1

        self.allSprites = None
        

#---------------------START MENU LOOP------------------------
#------------------------------------------------------------


    def startMenuLoop(self):
        """
        This is the loop for the starting menu of the game
        Args: None
        Return: None
        """
        
        self.allSprites = pygame.sprite.Group((self.startButton,) + (self.quitButton,))

        #event loop
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if self.startButton.rect.collidepoint(mouse):
                    self.state = "classMenu"
                elif self.quitButton.rect.collidepoint(mouse):
                    exit()

        #update models
        
        #redraw
        self.screen.blit(self.background1, (0,0))
        self.allSprites.draw(self.screen)
        
        #update screen
        pygame.display.flip()
            

#-----------------------CLASS MENU LOOP-----------------------
#-------------------------------------------------------------

    def classMenuLoop(self):
        """
        This is the loop to select the class you choose to play as in the game
        Args: None
        Return: None
        """
        samurai = hero.Hero('samurai', 500, 100, 200, 20, 800, 300, 'assets/samaraiSmall.png')
        samuraiButton = button.button(800, self.screenHeight*3/4, "Samurai", 48, (0,0,0), (255,255,255))
        ninja = hero.Hero('ninja', 300, 150, 70, 200, 400, 200, 'assets/ninja.png')
        ninjaButton = button.button(400, self.screenHeight*3/4, "Ninja", 40, (0,0,0), (255,255,255))

        self.allSprites = pygame.sprite.Group((samuraiButton,) + (samurai,) + (ninja,) + (ninjaButton,))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if samuraiButton.rect.collidepoint(mouse):
                    self.hero = samurai
                    self.heroHealthBar = healthBar.healthBar(1090, 30, self.hero.health, self.hero.max_health)
                    self.state = "battleLoop"
                elif ninjaButton.rect.collidepoint(mouse):
                    self.hero = ninja
                    self.heroHealthBar = healthBar.healthBar(1090, 30, self.hero.health, self.hero.max_health)
                    self.hero.rect.x = 850
                    self.hero.rect.y = 200
                    self.state = "battleLoop"

        #update data

        #redraw
        self.screen.blit(self.background2, (0,0))
        self.allSprites.draw(self.screen)
        #update screen
        pygame.display.flip()

#-----------------------------------------------------------------
#---------------------Bellow is Battle Loop-----------------------

    def battleLoop(self):
        """
        This is the loop that will handle the majority of the game's functionalities, including each
        battle, the mapping of each playthrough, and the turnbased combat
        Args: None
        Return: None
        """
        
        #pygame.mixer.music.load("assets/")

        i = -1
        enemiesAlive = self.enemyCount[i]
        #for loop for how many battles there are in the map
        for monsters in self.battles:
            allSprites = pygame.sprite.Group((self.hero,) + (monsters,) + (self.attackButton,) + (self.magicButton,) + (self.heroHealthBar,) + (self.itemButton,) + (self.defendButton,) + (self.dialogue,))

            i += 1
            enemiesAlive = self.enemyCount[i]
            print(f"battle {i+1}/3")
            for sprite in monsters:
                self.target = sprite

            #while loop to battle until victory or defeat
            while self.enemyCount[i] != 0 and self.state != "gameOver":

                #event loop
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        exit()
                    if e.type == pygame.MOUSEBUTTONDOWN:
                        mouse = pygame.mouse.get_pos()
                        if self.attackButton.rect.collidepoint(mouse):
                            #hero attack
                            self.hero.attack(self.target)
                            #monsters attack
                            #print monster attack to dialogue box once it works :)
                            for sprite in monsters:
                                if sprite.alive:
                                    sprite.attack(self.hero)
                        if self.magicButton.rect.collidepoint(mouse):
                            self.hero.useMagic(self.target, self.dialogue)
                            for sprite in monsters:
                                if sprite.alive:
                                    sprite.attack(self.hero)
                        if self.itemButton.rect.collidepoint(mouse):
                            itemUsage = self.hero.useItem()
                            if itemUsage == True:
                                for sprite in monsters:
                                    if sprite.alive:
                                        sprite.attack(self.hero)
                            else:
                                print("no more items")
                        if self.defendButton.rect.collidepoint(mouse):
                            self.hero.defending()
                            for sprite in monsters:
                                if sprite.alive:
                                    sprite.attack(self.hero)
                        else:
                            for sprite in monsters:
                                if sprite.rect.collidepoint(mouse):
                                    self.target = sprite


                #update models
                #health bar decrease
                self.hero.update()
                self.heroHealthBar.update(self.hero.health)

                #monster death check
                for sprite in monsters:
                    sprite.deathCheck()
                    if sprite.alive == False:
                        self.enemyCount[i] -=1
                        monsters.remove(sprite)
                        for sprite in monsters:
                            self.target = sprite

                #hero death check
                if self.hero.alive == False:
                    self.state = "gameOver"

                #redraw
                self.screen.blit(self.battleBackground, (0,0))
                self.screen.blit(self.moveBox, (1080, 0))
                self.screen.blit(self.dialogueBox, (0,580))
                allSprites.draw(self.screen)
        
                #update screen
                pygame.display.flip()

        if self.hero.alive:
            self.state = "victoryScreen"
        else:
            self.state = "gameOver"

#-----------------------------------------------------------------
#-----------------------------------------------------------------

    def gameOverLoop(self):
        """
        This is the loop for when you suck at this game
        Args: None
        Return: None
        """
        
        self.allSprites = pygame.sprite.Group((self.quitButton,) + (self.youSuck,))

        #event loop
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if self.quitButton.rect.collidepoint(mouse):
                    exit()
                elif self.youSuck.rect.collidepoint(mouse):
                    print("ur bad lol")

        #update models
        #save highscore if applicable

        #redraw
        self.screen.blit(self.deathBackground, (0,0))
        self.allSprites.draw(self.screen)
        
        #update screen
        pygame.display.flip()

#-----------------------------------------------------------------
#-----------------------------------------------------------------

    def victoryLoop(self):
        """
        This is the loop for when you are decent at gaming and you win
        Args: None
        Return: None
        """
        
        self.allSprites = pygame.sprite.Group((self.quitButton,) + (self.victory,))

        #event loop
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if self.quitButton.rect.collidepoint(mouse):
                    exit()
                elif self.victory.rect.collidepoint(mouse):
                    print("ur good lol")

        #update models
        #save highscore if applicable

        #redraw
        self.screen.blit(self.winBackground, (0,0))
        self.allSprites.draw(self.screen)
        
        #update screen
        pygame.display.flip()

#-----------------------------------------------------------------
#-----------------------------------------------------------------

    def mainloop(self):
        """
        This is the main loop of the game that manages every other loop
        Args: None
        Return: None
        """
        while self.state == "startMenu":
            self.startMenuLoop()
        while self.state == "classMenu":
            self.classMenuLoop()
        while self.state == "battleLoop":
            self.battleLoop()
        while self.state == "gameOver":
            self.gameOverLoop()
        while self.state == "victoryScreen":
            self.victoryLoop()
            
            
