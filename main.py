import pygame
from src import Controller

#class 
def main():
    pygame.init()
    team= {"lead": "Conner Smith", "backend": "Adejo", "frontend": "Connor Meybohm"}
    print("Software Lead is:", team["lead"])
    print("Backend is:", team["backend"])
    print("Frontend is:", team["frontend"])
    #Create an instance on your controller object
    game = Controller.Controller()
    #Call your mainloop
    game.mainloop()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 2 LINES OF CODE ######
main()
