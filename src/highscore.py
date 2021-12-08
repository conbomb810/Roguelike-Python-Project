import pygame
import json

#this is the overall highscore between playthroughs
#all this needs to do is import a highscore from a json file
class highscore(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        fptr = open("src/HighScore.json", 'r')
        self.font = pygame.font.SysFont("caladea", 35)
        info = json.load(fptr)
        self.score = info.get("highscore")
        fptr.close()
        self.scoreStr = f"HIGHSCORE: {self.score}"
        self.textbox = self.font.render(self.scoreStr, False, (0,0,0), (255,255,153))
        self.image = self.textbox
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.scoreDictionary = None
		
    def update(self, newScore):
        self.scoreStr = f"NEW HIGHSCORE: {newScore}"
        self.textbox = self.font.render(self.scoreStr, False, (0,0,0), (255,255,153))
        self.image = self.textbox
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.scoreDictionary = {"highscore":newScore}
        fptr = open("src/HighScore.json", 'w')
        json.dump(self.scoreDictionary, fptr)
        fptr.close()
