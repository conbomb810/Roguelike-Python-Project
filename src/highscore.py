#this is the overall highscore between playthroughs
class highscore:
    def __init__(self, x, y):
        super().__init__(self)  #doesnt work for some reason
        self.image = pygame.image.load("assets/tempHighScore.jpg").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.value = 100
		
    def getHighScore(self):
        pass
        #read in file data and attribute to self.value
