import pygame
from src import highscore
from src import hero
#from src import monster

class controller:
    def __init__(self):
        self.screenWidth = 1280
        self.screenHeight = 720
        
        pygame.init()
        self.state = "startMenu"
        

        #font stuff
        pygame.font.init()
        self.font = pygame.font.SysFont("caladea", 48)

        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.background = pygame.image.load("assets/mountainTestBackground.jpg").convert_alpha()

        
        self.highscore = highscore.highscore(500, 200)
        self.monsters = pygame.sprite.Group()
        

#------------------LOOPS BELOW------------------------
#-----------------------------------------------------


    def startMenuLoop(self):
        #initialization
        startButton = self.font.render("Start", False, (0,0,0), (255,255,255))
        startButtonCenter = startButton.get_rect(center=(self.screenWidth/2, self.screenHeight/2))


        #event loop
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= 400 and pygame.mouse.get_pos()[0] <= 600 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] >= 600:
                self.state = "classMenu"
                #exit()

        #update models
        
        #redraw
        self.screen.blit(self.background, (0,0))
        self.screen.blit(startButton, startButtonCenter)
        
        #update screen
        pygame.display.flip()
            

#-----------------------------------------------------------
#-----------------------------------------------------------

    def classMenuLoop(self):
        samurai = Hero('samurai', 500, 'health pot', 200)
        #test class
        #need to draw the hero and monsterssamurai
        #draw healthbars
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            #mouse cursor on selection boxes checks (each class and startgame button)

        #update data

        #redraw

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
            
            
