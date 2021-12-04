import pygame
#from src import highscore
from src import hero
from src import button
from src import monster
from src import healthBar

#LIST OF THINGS I CAN'T DO BECAUSE I DON'T HAVE THEIR MODELS/THEY ARENT WORKING:
#dialoguebox
#highscore
#score
#mana
#healthBar
#hero.item
#hero.magic
#hero.defend

#LIST OF THINGS I NEED TO WORK:
#monster removing it's own attack capabilities when alive = False

#LIST OF THINGS TO IMPLEMENT (not including the above):
#multiple enemies
#multiple fights
#animations?
#music

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
        self.monsters1 = pygame.sprite.Group()
        #import monsters1 2 and 3 from file
        self.monsters1.add(monster.monster(300, 50, 50))
        self.monsters1.add(monster.monster(300, 50, 150))
        self.monstersAlive1 = 2
        self.monsters2 = pygame.sprite.Group()
        self.monsters2.add(monster.monster(600, 50, 50))
        self.monsters3 = pygame.sprite.Group()
        self.monsters3.add(monster.monster(1000, 50, 50))
        self.monsters3.add(monster.monster(300, 50, 150))
        self.monster = monster.monster(300, 50, 50) #this is a test monster
        self.battles = [self.monsters1, self.monsters2, self.monsters3]

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
        samurai = hero.Hero('samurai', 500, 'health pot', 200) #this info will be imported from a JSON file
        samuraiButton = button.button(self.screenWidth/4, self.screenHeight*3/4, "Samurai", 48, (0,0,0), (255,255,255))
        self.allSprites = pygame.sprite.Group((samuraiButton,) + (samurai,))

        #test class
        #need to draw the hero and monsterssamurai
        #draw healthbars
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if samuraiButton.rect.collidepoint(mouse):
                    self.hero = samurai
                    self.heroHealthBar = healthBar.healthBar(1090, 30, self.hero.health, self.hero.max_health)
                    self.state = "battleLoop"
            #add more classes once we have it set up correctly

        #update data

        #redraw
        self.screen.blit(self.background2, (0,0))
        self.allSprites.draw(self.screen)
        #update screen
        pygame.display.flip()

#-----------------------------------------------------------------
#---------------------Bellow is Battle Loop-----------------------


    #MAKE USE OF UPDATE METHODS
    #USE THE UPDATE METHOD IN monster.py TO CHANGE ITS HEALTH ACCORDING TO DAMAGE TAKEN FROM PLAYER
    #USE THE UPDATE METHOD IN hero.py TO CHANGE ITS HEALTH ACCORDING TO DAMAGE TAKEN FROM MONSTERS
    """
    def playerTurnLoop(self):
        #actions allowed during player turn
        #event loop
        for e in range(10):#"HERO ACTIONS AMOUNT"):
            
            if e.type == pygame.QUIT:
                exit()
            #Check which action the user clicks, and use said action
        #need to add healthbar decrese when monster attacks

        #check if all monsters are dead, if not change to monsterTurnLoop
        numAlive = 0
        for i in self.monsters:
            if i.health >= 0:
                numAlive += 1
        if numAlive > 0:
            self.state = "monsterTurn"
        else:
            self.state = "mapLoop"



    def monsterTurnLoop(self):
        #enemy calculations, change healthbars, kill player
        #no event loop
        
        #monster actions
        self.dialoguebox.clear() #will clear the dialogue box text and stored string
        for i in self.monsters:
            i.attack() #will pick a move randomly and use it (i.e. attack player or heal self)
            #add to the text that will appear in the dialogue box
            self.dialoguebox.addToText(i) #this implies the use of __str__ in monster.py to be what dialogue box outputs
            
        #check if player is dead, if not change to playerTurnLoop
        if self.hero.health <= 0:
            self.state = "gameOver"
        else:
            self.state = "playerTurn"
    """
        
    def battleLoop(self):
        """
        This is the loop that will handle the majority of the game's functionalities, including each
        battle, the mapping of each playthrough, and the turnbased combat
        Args: None
        Return: None
        """
        #read in JSON file with all of the maps in the game and randomly pick one to use
        gameMap1 = pygame.sprite.Group()
        #gameMap2 = pygame.sprite.Group()
        #gameMap3 = pygame.sprite.Group()
        
        #the below is inputted via json file, this is just a test
        #FIND A WAY TO MAKE MULTIPLE MONSTERS WORK
        
        allSprites = pygame.sprite.Group((self.hero,) + (self.monsters1,) + (self.attackButton,) + (self.magicButton,) + (self.heroHealthBar,) + (self.itemButton,) + (self.defendButton,))

        #for loop for how many battles there are in the map
        for monsters in self.battles:
            #while loop to battle until victory or defeat
            while self.monstersAlive1 != 0:

                #event loop
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        exit()
                    if e.type == pygame.MOUSEBUTTONDOWN:
                        mouse = pygame.mouse.get_pos()
                        if self.attackButton.rect.collidepoint(mouse):
                            #hero attack
                            self.hero.attack(self.target)  #replace self.monster with self.target for multiple enemies
                            #monsters attack
                            #self.monsters1.update(self.hero)
                            self.monster.attack(self.hero) #print monster attack to dialogue box once it works :)
                        if self.magicButton.rect.collidepoint(mouse):
                            self.hero.magic(self.target)
                            self.monster.attack(self.hero)
                        if self.itemButton.rect.collidepoint(mouse):
                            self.hero.item(self.target)
                            self.monster.attack(self.hero)
                        if self.defendButton.rect.collidepoint(mouse):
                            self.hero.defend() #fix up later
                            self.monster.attack(self.hero)
                        else:
                            for sprite in monsters:
                                if sprite.rect.collidepoint(mouse):
                                    self.target = sprite


                #update models
                #health bar decrease
                self.hero.update()
                self.heroHealthBar.update(self.hero.health)

                #monster death check
                #self.monster.deathCheck()
                #if self.monster.alive == False:
                    #self.state = "victoryScreen"
                for sprite in self.monsters1:
                    if sprite.alive == False:
                        self.monstersAlive1 -=1
                        self.monsters1.remove(sprite)
                    #if self.monstersAlive1 == 0:
                        #self.state = "victoryScreen"

                #hero death check
                self.hero.update()
                if self.hero.alive == False:
                    self.state = "gameOver"

                #redraw
                self.screen.blit(self.battleBackground, (0,0))
                self.screen.blit(self.moveBox, (1080, 0))
                self.screen.blit(self.dialogueBox, (0,580))
                allSprites.draw(self.screen)
        
                #update screen
                pygame.display.flip()

        self.state = "victoryScreen"

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
        while self.state == "mapLoop":
            self.mapLoop()
            
            
