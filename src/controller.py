import pygame
from src import highscore
from src import hero
from src import button
#from src import monster

class controller:
    def __init__(self):
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


        self.hero = None        
        self.highscore = highscore.highscore(500, 200)
        self.monsters = pygame.sprite.Group()
        

#---------------------START MENU LOOP------------------------
#------------------------------------------------------------


    def startMenuLoop(self):
        startButton = button.button(self.screenWidth/2, self.screenHeight/2, "Start", 48, (0,0,0), (255,255,255))
        quitButton = button.button(self.screenWidth/2, self.screenHeight*3/4, "Quit", 48, (0,0,0), (255,0,0))
        allSprites = pygame.sprite.Group((startButton,) + (quitButton,))

        #event loop
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if startButton.rect.collidepoint(mouse):
                    self.state = "classMenu"
                elif quitButton.rect.collidepoint(mouse):
                    exit()

        #update models
        
        #redraw
        self.screen.blit(self.background1, (0,0))
        allSprites.draw(self.screen)
        
        #update screen
        pygame.display.flip()
            

#-----------------------CLASS MENU LOOP-----------------------
#-------------------------------------------------------------

    def classMenuLoop(self):
        samurai = hero.Hero('samurai', 500, 'health pot', 200) #this info will be imported from a JSON file
        samuraiButton = button.button(self.screenWidth/4, self.screenHeight*3/4, "Samurai", 48, (0,0,0), (255,255,255))
        allSprites = pygame.sprite.Group((samuraiButton,) + (samurai,))

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
                    print(self.hero)
                    self.state = "battleLoop"
            #add more classes once we have it set up correctly

        #update data

        #redraw
        self.screen.blit(self.background2, (0,0))
        allSprites.draw(self.screen)
        #update screen
        pygame.display.flip()

#-----------------------------------------------------------------
#---------------------Bellow is Battle Loop-----------------------


    #MAKE USE OF UPDATE METHODS
    #USE THE UPDATE METHOD IN monster.py TO CHANGE ITS HEALTH ACCORDING TO DAMAGE TAKEN FROM PLAYER
    #USE THE UPDATE METHOD IN hero.py TO CHANGE ITS HEALTH ACCORDING TO DAMAGE TAKEN FROM MONSTERS

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

        
        
            
    

    def battleLoop(self):
        #instantiate battle
        for e in range(10):#"IMPORT DATA FROM FILE"):
            pass#self.monsters.add(monster.monster("INSERT MONSTER DATA FROM FILE"))

        #this will be two different loops, playerTurnLoop and monsterTurnLoop
        while self.state == "playerTurn":
            playerTurnLoop()
        while self.state == "monsterTurn":
            monsterTurnLoop()

#-----------------------------------------------------------------
#-----------------------------------------------------------------

    def gameOverLoop(self):
        pass#loop for when player dies

    def mainloop(self):
        while self.state == "startMenu":
            self.startMenuLoop()
        while self.state == "classMenu":
            self.classMenuLoop()
        while self.state == "battleLoop":
            self.battleLoop()
        while self.state == "gameOver":
            self.gameOverLoop()
        while self.state == "mapLoop":
            self.mapLoop()
            
            
